from abc import ABC, abstractmethod
from business_rule_engine.classes import Facts


class Rule(ABC):

    @abstractmethod
    def perform(self, facts: Facts) -> None:
        raise NotImplementedError
