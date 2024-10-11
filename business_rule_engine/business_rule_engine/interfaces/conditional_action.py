from abc import ABC, abstractmethod

from business_rule_engine.classes import Facts


class ConditionalAction(ABC):

    @abstractmethod
    def evaluate(self, facts: Facts) -> bool:
        raise NotImplementedError

    @abstractmethod
    def perform(self, facts: Facts) -> None:
        raise NotImplementedError
