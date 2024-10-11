from typing import Optional
from tests.conftest import other_endpoint, receiver_endpoint, twootr
from tests.resources import TestData
from twootr.classes import Position, Twoot

from twootr.twootr import Twootr
from twootr.classes import SenderEndpoint
from twootr.classes.receiver_endpoint import ReceiverEndpoint
from twootr.interfaces import FollowStatus
from unittest.mock import MagicMock



class TestActions:

    __POSITION_1: Position = Position(0)
    __twootr: Twootr = Twootr()
    __twoot_repository = None
    __endpoint: SenderEndpoint
    __receiver_endpoint: ReceiverEndpoint = MagicMock(ReceiverEndpoint())

    def test_should_follow_valid_user(self):
        self.__log_on()
        follow_status: FollowStatus = self.__endpoint.on_follow(TestData.OTHER_USER_ID)
        assert FollowStatus.SUCCESS == follow_status

    def test_should_not_duplicate_follow_valid_user(self, endpoint: SenderEndpoint):
        self.__log_on()
        follow_status: FollowStatus = self.__endpoint.on_follow(TestData.OTHER_USER_ID)
        assert FollowStatus.ALREADY_FOLLOWING == follow_status

    def test_should_follow_invalid_user(self):
        self.__log_on()
        follow_status: FollowStatus = self.__endpoint.on_follow("INVALID_USER_ID")
        assert FollowStatus.INVALID_USER == follow_status

    def test_should_receive_twoots_from_followed_user(self):
        id_: str = "1"

        self.__log_on()
        self.__endpoint.on_follow(TestData.OTHER_USER_ID)

        other_endpoint: SenderEndpoint = self.__other_log_on()
        other_endpoint.on_send_twoot(id_, TestData.TWOOT)

        self.__twoot_repository.add.assert_called_once_with(id_, TestData.OTHER_USER_ID, TestData.TWOOT)
        receiver_endpoint.on_twoot.assert_called_once_with(Twoot(id_, TestData.OTHER_USER_ID, TestData.TWOOT))

    def test_should_receive_replay_of_twoots_after_user_log_off(self, follows_other_user, other_endpoint: SenderEndpoint, endpoint: SenderEndpoint):
        id_: str = "1"
        self.__user_follows_other_user()

        other_endpoint: SenderEndpoint = self.__other_log_on()
        other_endpoint.on_send_twoot(id_, TestData.TWOOT)

        self.__log_on()

        self.__receiver_endpoint.on_twoot.assert_called_once_with(TestData.twoot_at(id_, self.__POSITION_1))

    def __user_follows_other_user(self):
        self.__log_on()
        self.__endpoint.on_follow(TestData.OTHER_USER_ID)
        self.__endpoint.logoff()

    def __other_log_on(self):
        return self.__log_on(TestData.OTHER_USER_ID, MagicMock(ReceiverEndpoint()))

    def __log_on(self, user_id: str = TestData.USER_ID, receiver_endpoint: ReceiverEndpoint = None) -> SenderEndpoint:
        if receiver_endpoint is None:
            receiver_endpoint = self.__receiver_endpoint
        sender_endpoint: Optional[SenderEndpoint] = self.__twootr.on_logon(user_id, TestData.PASSWORD, receiver_endpoint)
        assert sender_endpoint is not None, "Failed to logon"
        return sender_endpoint
