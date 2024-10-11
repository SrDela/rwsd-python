from abc import ABC, abstractmethod
from business_rule_engine.classes import Facts


class Condition(ABC):

    @abstractmethod
    def evaluate(self, facts: Facts) -> bool:
        raise NotImplementedError
