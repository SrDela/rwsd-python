from typing import List
from decimal import Decimal

from bank_analyzer.classes.bank_statement_processor import BankStatementProcessor
from bank_analyzer.classes.parser.csv import BankStatementCSVParser
from bank_analyzer.classes.bank_transaction import BankTransaction
from bank_analyzer.interfaces.bank_transaction import Month

parser: BankStatementCSVParser = BankStatementCSVParser()
lines: List[str] = [
    "30-01-2017,-50,Tesco",
    "01-04-2017,6000,Salary",
    "02-04-2017,-4000,Rent",
    "19-10-2017,-210,Tesco",
]
bank_transactions = parser.parseLinesFrom(lines)


class TestBankStatementProcessor:

    processor: BankStatementProcessor = BankStatementProcessor(bank_transactions)

    def test_processor_calculates_total_correctly(self):
        total: Decimal = self.processor.summarize_transactions(
            lambda accumulator, bank_transaction: accumulator + bank_transaction.amount
        )
        expected: Decimal = Decimal(1740)
        assert expected == total

    def test_processor_calculates_total_in_month_correctly(self):
        total: Decimal = self.processor.calculate_total_in_month(Month.APRIL)
        expected: Decimal = Decimal(2000)
        assert expected == total

    def test_processor_calculates_total_for_category_correctly(self):
        total: Decimal = self.processor.summarize_transactions(
            lambda accumulator, bank_transaction: (
                accumulator + bank_transaction.amount
                if bank_transaction.description == 'Tesco'
                else accumulator
            )
        )
        expected: Decimal = Decimal(-260)
        assert expected == total

    def test_find_transactions_correctly(self):
        transactions: List[BankTransaction] = self.processor.find_transactions(
            lambda bank_transaction: bank_transaction.description == "Tesco"
        )
        assert len(transactions) == 2
        assert transactions[0].amount == Decimal(-50)
        assert transactions[1].amount == Decimal(-210)

    def test_find_transactions_greater_than_equal_correctly(self):
        transactions: List[BankTransaction] = self.processor.find_transactions_greater_than_equal(Decimal(0))
        assert len(transactions) == 1
