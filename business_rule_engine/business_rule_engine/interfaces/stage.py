from decimal import Decimal
from enum import Enum


class Stage(Enum):
    LEAD: Decimal = Decimal(0.2)
    INTERESTED: Decimal = Decimal(0.5)
    EVALUATING: Decimal = Decimal(0.8)
    CLOSED: Decimal = Decimal(1)
