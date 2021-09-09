import argparse

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
