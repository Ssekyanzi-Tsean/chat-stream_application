import pytest
from unittest import mock
from unittest.mock import MagicMock, create_autospec


@pytest.fixture
def serverName():
    return str('localhost:9091')


@pytest.fixture
def channelName():
    return str('message-chat-1')


# @mock.patch('app.main.delivery_report')
def test_run_producer_output():
    """Run producer function"""
    from app.main import run_producer
    mock_function = create_autospec(run_producer, return_value={
                                    'id': '12', 'name': 'samuel'})
    serverName1 = 'localhost:9092'
    channelName2 = 'message-chat-1'
    delivery_mock = MagicMock(side_effect=delivery_report)
    assert run_producer(serverName1, channelName2) == {
        'id': 10, 'name': "Micheal"}
