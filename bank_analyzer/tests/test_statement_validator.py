from bank_analyzer.classes.validator.bank_statement import BankStatementValidator
from bank_analyzer.classes.notification import Notification
from bank_analyzer.classes.validator import (
    INVALID_DATE_FORMAT_ERR, INVALID_AMOUNT_FORMAT_ERR,
    FUTURE_DATE_ERR, TOO_LONG_DESCRIPTION_ERR
)


class TestBankStatementValidator:

    def test_validates_correctly_with_no_errors(self):
        validator: BankStatementValidator = BankStatementValidator(
            amount="-140",
            date_="10-03-2024",
            description="Lorem ipsum"
        )
        results: Notification = validator.validate()
        assert not results.has_errors()

    def test_fails_for_too_long_description(self):
        validator: BankStatementValidator = BankStatementValidator(
            amount="2000",
            date_="10-03-2024",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque posuere urna non accumsan cras amet."
        )
        results: Notification = validator.validate()
        expected_message = TOO_LONG_DESCRIPTION_ERR
        assert len(results.errors) == 1
        assert expected_message == results.errors[0]

    def test_fails_for_incorrect_date_format(self):
        validator: BankStatementValidator = BankStatementValidator(
            amount="2000",
            date_="2024-03-10",
            description="Lorem ipsum"
        )
        results: Notification = validator.validate()
        expected_message = INVALID_DATE_FORMAT_ERR
        assert len(results.errors) == 1
        assert expected_message == results.errors[0]

    def test_fails_for_future_date(self):
        validator: BankStatementValidator = BankStatementValidator(
            amount="2000",
            date_="10-03-3000",
            description="Lorem ipsum"
        )
        results: Notification = validator.validate()
        expected_message = FUTURE_DATE_ERR
        assert len(results.errors) == 1
        assert expected_message == results.errors[0]

    def test_fails_for_incorrect_amount_format(self):
        validator: BankStatementValidator = BankStatementValidator(
            amount="asdw",
            date_="10-03-2024",
            description="Lorem ipsum"
        )
        results: Notification = validator.validate()
        expected_message = INVALID_AMOUNT_FORMAT_ERR
        assert len(results.errors) == 1
        assert expected_message == results.errors[0]

    def test_fails_for_multiple_fields(self):
        validator: BankStatementValidator = BankStatementValidator(
            amount="asdw",
            date_="10-03-2024",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque posuere urna non accumsan cras amet."
        )
        results: Notification = validator.validate()
        assert len(results.errors) == 2
