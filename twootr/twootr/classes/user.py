from __future__ import annotations
from typing import Optional, Set

from twootr.interfaces.follow_status import FollowStatus
from .position import Position
from .twoot import Twoot
from .receiver_endpoint import ReceiverEndpoint


class User:

    def __init__(
        self,
        id_: str,
        password: bytes,
        salt: bytes,
        last_seen_position: Position
    ) -> None:
        self.__id: str = id_
        self.__password: bytes = password
        self.__salt: bytes = salt
        self.__last_seen_position: Position = last_seen_position
        self.__followers: Set[User] = set()
        self.__following: Set[str] = set()

        self.__receiver_endpoint: Optional[ReceiverEndpoint] = None

    @property
    def password(self) -> bytes:
        return self.__password

    @property
    def salt(self) -> bytes:
        return self.__salt

    @property
    def id_(self) -> str:
        return self.__id

    def receive_twoot(self, twoot: Twoot) -> bool:
        if self.is_logged_on():
            self.__receiver_endpoint.on_twoot(twoot)
            self.__last_seen_position = twoot.position
            return True
        return False

    def is_logged_on(self) -> bool:
        return self.__receiver_endpoint is not None

    def add_follower(self, user: User) -> FollowStatus:
        if user not in self.__followers:
            self.__followers.add(user)
            return FollowStatus.SUCCESS

        return FollowStatus.ALREADY_FOLLOWING

    def on_logon(self, receiver_endpoint: ReceiverEndpoint) -> None:
        self.__receiver_endpoint = receiver_endpoint

    def on_logoff(self) -> None:
        self.__receiver_endpoint = None

    @property
    def followers(self) -> Set[User]:
        return self.__followers

    @property
    def following(self) -> Set[str]:
        return self.__following

    @property
    def last_seen_position(self) -> Position:
        return self.__last_seen_position

    def __str__(self) -> str:
        return f"User<id={self.__id}>"
