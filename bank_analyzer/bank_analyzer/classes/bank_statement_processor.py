from typing import List, Union
from decimal import Decimal

from bank_analyzer.classes.bank_transaction import BankTransaction
from bank_analyzer.classes.summary import SummaryStatistics
from bank_analyzer.interfaces import (
    BankTransactionFilter, BankTransactionSummarizer, 
    Month
)


class BankStatementProcessor:

    def __init__(self, bank_transactions: List[BankTransaction]):
        self.__bank_transactions: List[BankTransaction] = bank_transactions

    def summarize_transactions(
        self, 
        bank_transaction_summarizer: BankTransactionSummarizer
    ) -> Decimal:
        result: Decimal = Decimal(0)
        for bank_transaction in self.__bank_transactions:
            result = bank_transaction_summarizer(result, bank_transaction)
        return result

    def summary_statistics(self) -> SummaryStatistics:
        total = self.summarize_transactions(lambda acc, bank_transaction: acc + bank_transaction.amount)
        return SummaryStatistics(
            sum_=total,
            max_=self.summarize_transactions(lambda acc, bank_transaction: acc if acc > bank_transaction.amount else bank_transaction.amount),
            min_=self.summarize_transactions(lambda acc, bank_transaction: acc if acc < bank_transaction.amount else bank_transaction.amount),
            average=total/len(self.__bank_transactions)
        )

    def calculate_total_in_month(self, month: Month) -> Decimal:
        bank_transaction_summarizer: BankTransactionSummarizer = (
            lambda accumulator, bank_transaction: (
                accumulator + bank_transaction.amount 
                if bank_transaction.local_date.month == month.value
                else accumulator
            )
        )
        return self.summarize_transactions(bank_transaction_summarizer)

    def find_transactions(self, bank_transaction_filter: BankTransactionFilter) -> List[BankTransaction]:
        result: List[BankTransaction] = []
        for bank_transaction in self.__bank_transactions:
            if bank_transaction_filter(bank_transaction):
                result.append(bank_transaction)
        return result

    def find_transactions_greater_than_equal(self, amount: Decimal) -> List[BankTransaction]:
        return self.find_transactions(lambda bank_transaction: bank_transaction.amount >= amount)
