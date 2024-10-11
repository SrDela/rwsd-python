from twootr.interfaces.follow_status import FollowStatus
from twootr.twootr import Twootr
from .user import User


class SenderEndpoint:

    def __init__(self, user: User, twootr: Twootr) -> None:
        self.__user: User = user
        self.__twootr: Twootr = twootr

    def on_follow(self, user_id_to_follow: str) -> FollowStatus:
        return self.__twootr.on_follow(self.__user, user_id_to_follow)

    def on_send_twoot(self, id_: str, content: str) -> None:
        pass
