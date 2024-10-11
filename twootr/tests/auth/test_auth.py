from typing import Optional
from tests.resources import TestData

from twootr.classes import SenderEndpoint, ReceiverEndpoint
from twootr.twootr import Twootr

twt = Twootr()
receiver_endpoint = ReceiverEndpoint()

class TestAuth:

    def should_be_able_to_authenticate_user(self):
        # Receive logon message for valid user
        # Logon method returns new endpoint
        endpoint: Optional[SenderEndpoint] = twt.on_logon(
            user_id=TestData.USER_ID,
            password=TestData.PASSWORD,
            receiver=receiver_endpoint
        )
        # Assert that endpoint is valid
        assert endpoint is not None

    def should_not_authenticate_unknown_user(self):
        endpoint: Optional[SenderEndpoint] = twt.on_logon(
            user_id="unknown_user",
            password=TestData.PASSWORD,
            receiver=receiver_endpoint
        )
        assert endpoint is None

    def should_not_authenticate_with_wrong_password(self):
        endpoint: Optional[SenderEndpoint] = twt.on_logon(
            user_id=TestData.USER_ID,
            password="bad_password",
            receiver=receiver_endpoint
        )
        assert endpoint is None
