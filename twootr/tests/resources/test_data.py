from twootr.classes import Position, Twoot


class TestData:

    USER_ID = ""
    PASSWORD = ""
    OTHER_USER_ID = ""
    TWOOT = ""

    @classmethod
    def twoot_at(cls, id_: str, position: Position) -> Twoot:
        return Twoot(id_, cls.OTHER_USER_ID, cls.TWOOT, position)
