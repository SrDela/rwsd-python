from bank_analyzer.classes.parser.csv import BankStatementCSVParser
from bank_analyzer.classes.bank_transaction import BankTransaction
from decimal import Decimal
from datetime import datetime
from typing import List


class TestBankStatementCSVParser:

    parser: BankStatementCSVParser = BankStatementCSVParser()

    def test_should_parse_one_line_correctly(self):
        line: str = "30-01-2017,-50,Tesco"
        result: BankTransaction = self.parser.parseFrom(line)

        expected: BankTransaction = BankTransaction(
            local_date=datetime.strptime('30-01-2017', '%d-%m-%Y').date(),
            amount=Decimal(-50), 
            description="Tesco"
        )
        # tolerance: Decimal = Decimal(0)

        assert result == expected

    def test_should_parse_multiple_lines_correctly(self):
        lines: List[str] = [
            "30-01-2017,-50,Tesco",
            "01-02-2017,6000,Salary",
            "02-02-2017,-4000,Rent"
        ]
        result: List[BankTransaction] = self.parser.parseLinesFrom(lines)

        expected_line1: BankTransaction = BankTransaction(
            local_date=datetime.strptime('30-01-2017', '%d-%m-%Y').date(),
            amount=Decimal(-50), 
            description="Tesco"
        )
        expected_line2: BankTransaction = BankTransaction(
            local_date=datetime.strptime('01-02-2017', '%d-%m-%Y').date(),
            amount=Decimal(6000), 
            description="Salary"
        )
        expected_line3: BankTransaction = BankTransaction(
            local_date=datetime.strptime('02-02-2017', '%d-%m-%Y').date(),
            amount=Decimal(-4000), 
            description="Rent"
        )

        assert result[0] == expected_line1
        assert result[1] == expected_line2
        assert result[2] == expected_line3
