import pytest
from unittest.mock import MagicMock
from tests.resources import test_data

from twootr.twootr import Twootr
from twootr.classes import ReceiverEndpoint, SenderEndpoint


@pytest.fixture()
def twootr() -> Twootr:
    return Twootr()


@pytest.fixture(autouse=True)
def receiver_endpoint() -> MagicMock:
    return MagicMock(ReceiverEndpoint())


@pytest.fixture()
def endpoint(twootr: Twootr, receiver_endpoint: MagicMock) -> SenderEndpoint:

    endpoint: SenderEndpoint = twootr.on_logon(
        user_id=test_data.USER_ID,
        password=test_data.PASSWORD,
        receiver=receiver_endpoint
    )
    return endpoint

@pytest.fixture()
def other_endpoint(twootr: Twootr) -> SenderEndpoint:
    receiver_endpoint: ReceiverEndpoint = ReceiverEndpoint()
    endpoint: SenderEndpoint = twootr.on_logon(
        user_id=test_data.OTHER_USER_ID,
        password=test_data.PASSWORD,
        receiver=receiver_endpoint
    )
    return endpoint
