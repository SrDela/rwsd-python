from enum import IntEnum
from decimal import Decimal
from typing import Callable

from bank_analyzer.classes.bank_transaction import BankTransaction


class Month(IntEnum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


BankTransactionFilter = Callable[[BankTransaction], bool]
BankTransactionSummarizer = Callable[[Decimal, BankTransaction], Decimal]
