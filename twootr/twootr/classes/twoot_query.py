from __future__ import annotations
from typing import Set
from .position import Position


class TwootQuery:

    def __init__(self) -> None:
        self.__in_users: Set[int] = {}
        self.__last_seen_position: Position = Position(-1)

    @property
    def in_users(self) -> Set[int]:
        return self.__in_users

    @property
    def last_seen_position(self) -> Position:
        return self.__last_seen_position

    def in_users(self, in_users: Set[int]) -> TwootQuery:
        self.__in_users = in_users
        return self

    def last_seen_position(self, last_seen_position: Position) -> TwootQuery:
        self.__last_seen_position = last_seen_position
        return self

    def has_users(self) -> bool:
        return len(self.__in_users) > 0
