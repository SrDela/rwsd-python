from abc import ABC, abstractmethod
from typing import Optional

from .follow_status import FollowStatus
from .consumer import Consumer

from twootr.classes import TwootQuery, Twoot


class TwootRepository(ABC):

    @abstractmethod
    def add(self, id_: str, user_id: str, content: str) -> Twoot:
        raise NotImplementedError

    @abstractmethod
    def get(self, id_: str) -> Optional[Twoot]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, twoot: Twoot) -> None:
        raise NotImplementedError

    @abstractmethod
    def query(self, twoot_query: TwootQuery, callback: Consumer[Twoot]) -> FollowStatus:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError


TwootRepository().query(
    TwootQuery().in_users(User).last_seen_position(position)
)