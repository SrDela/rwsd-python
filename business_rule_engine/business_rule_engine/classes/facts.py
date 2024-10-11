from typing import Dict


class Facts:

    def __init__(self) -> None:
        self.__facts: Dict[str, str] = {}

    def get_fact(self, name: str) -> str:
        return self.__facts.get(name, '')

    def add_fact(self, name: str, value: str) -> None:
        self.__facts[name] = value
