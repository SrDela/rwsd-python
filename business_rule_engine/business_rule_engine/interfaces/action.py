from abc import ABC, abstractmethod
from business_rule_engine.classes import Facts


class Action(ABC):

    @abstractmethod
    def execute(self, facts: Facts) -> None:
        raise NotImplementedError
