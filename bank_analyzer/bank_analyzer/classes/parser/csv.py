from datetime import datetime
from decimal import Decimal
from typing import List

from ._default import DATE_STR_FORMAT
from bank_analyzer.classes.bank_transaction import BankTransaction
from bank_analyzer.interfaces.bank_statement import BankStatementParser


class BankStatementCSVParser(BankStatementParser):

    def __init__(self):
        self.__separator = ","
        self.__date_format = DATE_STR_FORMAT

    def parseFrom(self, line: str) -> BankTransaction:
        columns = line.split(self.__separator)
        date_ = datetime.strptime(columns[0], self.__date_format).date()
        amount = Decimal(columns[1])
        description = columns[2]
        return BankTransaction(date_, amount, description)

    def parseLinesFrom(self, lines: List[str]) -> List[BankTransaction]:
        bank_transactions: List[BankTransaction] = []
        for line in lines:
            bank_transactions.append(self.parseFrom(line))
        return bank_transactions
