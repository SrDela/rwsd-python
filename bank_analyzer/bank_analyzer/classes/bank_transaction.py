from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class BankTransaction:
    local_date: date
    amount: Decimal
    description: str

    def __eq__(self, value: any):

        if value is None or not isinstance(value, BankTransaction):
            return False
        return (
            value.amount == self.amount
            and value.local_date == self.local_date
            and value.description == self.description
        )
