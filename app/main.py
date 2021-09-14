from confluent_kafka import Producer
import argparse
from confluent_kafka import Consumer, KafkaException
from faker import Faker
from random import randint

parser = argparse.ArgumentParser(
    prog='Chatapp', description='Message Application')
sender = parser.add_argument_group(
    'sending', 'The following flags send your message')
sender.add_argument('--send', help='insert your message here', nargs='+')
sender.add_argument(
    '--server', help='select server to send messages through', nargs='?')
sender.add_argument(
    '--channel', help='select the topic name to send messages to', nargs='?')
receiver = parser.add_argument_group(
    'receiving', 'The following flags receive messages')
receiver.add_argument('receive', help='receiver flag', nargs='?')
receiver.add_argument('--group', help='The group to receive from')
receiver.add_argument(
    '--start', help='choose either "latest" or "earliest to select the messages to receive"')
args = parser.parse_args()


def run_producer(serverName, channelName):
    """The producer Function """
    p = Producer({'bootstrap.servers': serverName,
                  'acks': '-1', 'partitioner': 'consistent_random', 'batch.num.messages': '100',
                  'linger.ms': '3000'})

    #msg_value = args.send
    for i in range(0, 100):
        msg_value = {'id': randint(0, 100), 'name': Faker('en_US').name()}
    while True:
        try:
            # p.poll(timeout=0)
            p.produce(topic=channelName, value=str(msg_value),
                      on_delivery=delivery_report)
            break
        except BufferError as buffer_error:
            print(f"{buffer_error} :: waiting until the Queue gets some free space")
    p.flush()
    return msg_value


def delivery_report(err, msg):
    if err:
        return(f"Message delivery failed : {str(err)}")
    else:
        return(
            f"Message is delivered to the partition {msg.partition()}; Offset - {msg.offset()}")
        print(f"{msg.value()}")


def run_consumer(severName, groupId, offset, channelName):
    """The Consumer Function"""
    c = Consumer({'bootstrap.servers': severName,
                  'group.id': groupId,
                  'auto.offset.reset': offset})
    c.subscribe([channelName])
    try:
        while True:
            msg = c.poll(timeout=1.0)

            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                print(msg.value())

    except KeyboardInterrupt:
        print("Aborted by user")
    finally:
        c.close()
    return (msg.value)
