from app.main import run_consumer, run_producer
import pytest
from unittest import mock
from unittest.mock import MagicMock, create_autospec, patch, Mock


# @pytest.mark.skip(reason='')


@mock.patch('app.main.BufferError')
@mock.patch('app.main.generate_integer')
@mock.patch('app.main.generate_name')
@mock.patch('app.main.Producer')
def test_run_producer_output(ProducerMock, nameMock, integerMock, BufferMock):
    """Run producer function"""
    # Prepare
    severName = "localhost:9090"
    channelName = "channel-1"
    integerMock.return_value = 50
    nameMock.return_value = 'Micheal'
    buff = Mock()
    buff.side_effect = BufferError('Erroring')

    # Test
    response = run_producer(severName, channelName)
    BufferMock()
    # Assertion
    assert response == {'id': 50, 'name': 'Micheal'}
    BufferMock.assert_called_once()


# @pytest.mark.skip(reason='')
def test_delivery_report_on_error():
    from app.main import delivery_report
    delivery_report(err=BufferError, msg='missing')
    err = KeyError
    assert delivery_report(
        err, msg='hello world') == f'Message delivery failed : {str(err)}'


# @pytest.mark.skip(reason='')
@mock.patch('app.main.KafkaException')
@mock.patch('app.main.Consumer')
def test_run_consumer(ConsumerMock, KafkaExMock,):
    """Testing the Consumer Function"""
    from app.main import Consumer
    from confluent_kafka import KafkaException
    # Prepare
    severName = 'localhost:9092'
    groupId = 'chatgroup-1'
    offset = 'beginning'
    channelName = 'messages-1'
    SubscribeMock = channelName
    kafka_err = Mock()
    kafka_err.side_effect = Exception('KafkaExecption')
    # Test
    build = run_consumer(severName, groupId, offset, channelName)
    # Assertion
    assert build == ''
    kafka_err.assert_called()
