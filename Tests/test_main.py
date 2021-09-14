
import pytest
from unittest import mock
from unittest.mock import MagicMock, create_autospec, patch


@mock.patch('app.main.Producer')
@mock.patch('app.main.delivery_report')
def test_run_producer_output(deliveryMock, producerMock):
    """Run producer function"""
    from app.main import run_producer
    mock_function = create_autospec(run_producer, return_value={
        'id': 12, 'name': 'Micheal'})

    serverName1 = 'localhost:9092'
    channelName2 = 'message-chat-1'
    mock_function(serverName1, channelName2)
    from app.main import delivery_report
    delivery_mock = MagicMock(side_effect=delivery_report)
    assert mock_function(serverName1, channelName2) == {
        'id': 12, 'name': "Micheal"}


def test_delivery_report():
    from app.main import delivery_report
    delivery_report(err=BufferError, msg='missing')
