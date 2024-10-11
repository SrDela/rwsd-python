from __future__ import annotations


class Position:

    def __init__(self, value: int) -> None:
        self.__value: int = value
        self.__INITIAL_POSITION: Position = Position(-1)

    @property
    def value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        return f"Position<value={self.__value}>"

    def __eq__(self, __o: object) -> bool:
        if __o is None or not isinstance(__o, Position):
            return False
        return __o.value == self.value

    def __hash__(self) -> int:
        return self.__value

    def next_(self) -> Position:
        return Position(self.__value + 1)
