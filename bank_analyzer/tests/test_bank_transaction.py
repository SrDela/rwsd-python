from datetime import datetime
from decimal import Decimal

from bank_analyzer.classes.bank_transaction import BankTransaction


class TestBankTransaction:

    def test_equals_correctly(self):
        first_transaction = BankTransaction(
            local_date=datetime.strptime('2021-09-10', '%Y-%m-%d').date(),
            amount=Decimal(200),
            description="Test"
        )
        second_transaction = BankTransaction(
            local_date=datetime.strptime('2021-09-10', '%Y-%m-%d').date(),
            amount=Decimal(200),
            description="Test"
        )

        assert first_transaction.local_date == second_transaction.local_date
        assert first_transaction.amount == second_transaction.amount
        assert first_transaction.description == second_transaction.description
        assert first_transaction == second_transaction

    def test_equals_fails_correctly(self):
        first_transaction = BankTransaction(
            local_date=datetime.strptime('2021-09-10', '%Y-%m-%d').date(),
            amount=Decimal(200),
            description="Test"
        )
        second_transaction = BankTransaction(
            local_date=datetime.strptime('2021-09-10', '%Y-%m-%d').date(),
            amount=Decimal(500),
            description="Test"
        )

        assert first_transaction.local_date == second_transaction.local_date
        assert first_transaction.amount != second_transaction.amount
        assert first_transaction.description == second_transaction.description
        assert first_transaction != second_transaction

    def test_equals_fails_for_non_transaction_object(self):
        transaction = BankTransaction(
            local_date=datetime.strptime('2021-09-10', '%Y-%m-%d').date(),
            amount=Decimal(200),
            description="Test"
        )

        assert transaction != "fake_transaction"
