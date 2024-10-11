from typing import List

from bank_analyzer.classes.bank_statement_processor import BankStatementProcessor
from bank_analyzer.classes.bank_transaction import BankTransaction
from bank_analyzer.classes.summary import SummaryStatistics
from bank_analyzer.interfaces import BankStatementParser, Exporter, BankTransactionSummarizer


class BankStatementAnalyzer:

    def analyze(self, filepath: str, parser: BankStatementParser, exporter: Exporter) -> None:

        with open(filepath, 'r') as f:
            lines: List[str] = f.readlines()

        bank_transactions: List[BankTransaction] = parser.parseLinesFrom(lines)
        bank_statement_processor: BankStatementProcessor = BankStatementProcessor(bank_transactions)
        summary_statistics: SummaryStatistics = bank_statement_processor.summary_statistics()
        print(exporter.export(summary_statistics))
        return
