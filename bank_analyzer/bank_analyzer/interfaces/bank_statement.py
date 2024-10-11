from abc import ABC, abstractmethod
from typing import List
from bank_analyzer.classes.bank_transaction import BankTransaction


class BankStatementParser(ABC):

    @abstractmethod
    def parseFrom(self, line: str) -> BankTransaction:
        raise NotImplementedError

    @abstractmethod
    def parseLinesFrom(self, lines: List[str]) -> List[BankTransaction]:
        raise NotImplementedError
