from business_rule_engine.interfaces import Rule, Condition, Action
from .facts import Facts


class DefaultRule(Rule):

    def __init__(self, condition: Condition, action: Action) -> None:
        self.__condition: Condition = condition
        self.__action: Action = action

    def perform(self, facts: Facts) -> None:
        if self.__condition.evaluate(facts):
            self.__action.execute(facts)
        return
