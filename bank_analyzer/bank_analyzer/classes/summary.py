from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass
class SummaryStatistics:
    sum_: Decimal
    max_: Decimal
    min_: Decimal
    average: Decimal

    def asdict(self):
        return asdict(self)
