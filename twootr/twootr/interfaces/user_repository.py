from abc import ABC, abstractmethod
from typing import Optional
from twootr.classes import User
from .follow_status import FollowStatus


class UserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def follow(self, follower: User, user_to_follow: User) -> FollowStatus:
        raise NotImplementedError
