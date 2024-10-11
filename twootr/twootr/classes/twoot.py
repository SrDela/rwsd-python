from .position import Position


class Twoot:

    def __init__(self, id_: str, sender_id: str, content: str, position: Position) -> None:
        self.__id: str = id_
        self.__sender_id: str = sender_id
        self.__content: str = content
        self.__position: Position = position

    def is_after(self, other_position: Position) -> bool:
        return self.__position.value > other_position.value

    @property
    def id_(self) -> str:
        return self.__id

    @property
    def sender_id(self) -> str:
        return self.__sender_id

    @property
    def content(self) -> str:
        return self.__content

    @property
    def position(self) -> Position:
        return self.__position

    def __eq__(self, __o: object) -> bool:
        if __o is not None and not isinstance(__o, Twoot):
            return False
        return self.__id == __o.id_

    def __hash__(self) -> int:
        return self.__id.__hash__()

    def __str__(self) -> str:
        return (
            "<Twoot "
            f"id={self.__id}, "
            f"sender_id={self.__sender_id}, "
            f"content={self.__content}, "
            f"position={self.__position}"
            ">"
        )
