from typing import List


class Notification:

    def __init__(self) -> None:
        self.__errors: List[str] = []

    @property
    def errors(self) -> List[str]:
        return self.__errors

    def add_error(self, message: str) -> None:
        self.__errors.append(message)

    def has_errors(self) -> bool:
        return len(self.__errors) > 0

    def error_message(self) -> str:
        return " | ".join(self.__errors)
