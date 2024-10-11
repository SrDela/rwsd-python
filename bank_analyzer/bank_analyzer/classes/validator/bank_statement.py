from decimal import Decimal, InvalidOperation
from datetime import date, datetime

from ._default import (
    TOO_LONG_DESCRIPTION_ERR, INVALID_DATE_FORMAT_ERR, 
    FUTURE_DATE_ERR, INVALID_AMOUNT_FORMAT_ERR
)
from bank_analyzer.classes.notification import Notification
from bank_analyzer.classes.parser import DATE_STR_FORMAT


class BankStatementValidator:

    def __init__(
        self,
        amount: str,
        date_: str,
        description: str
    ) -> None:
        self.__amount: str = amount
        self.__date: str = date_
        self.__description: str = description

    def validate(self) -> Notification:

        notification: Notification = Notification()

        if len(self.__description) > 100:
            notification.add_error(TOO_LONG_DESCRIPTION_ERR)

        try:
            parsed_date: date = datetime.strptime(self.__date, DATE_STR_FORMAT).date()

            if parsed_date > date.today():
                notification.add_error(FUTURE_DATE_ERR)
        except ValueError:
            notification.add_error(INVALID_DATE_FORMAT_ERR)

        try:
            parsed_amount: Decimal = Decimal(self.__amount)
        except InvalidOperation:
            notification.add_error(INVALID_AMOUNT_FORMAT_ERR)

        return notification
