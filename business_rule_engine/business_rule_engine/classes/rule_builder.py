from __future__ import annotations
from typing import TYPE_CHECKING
from .rule import DefaultRule

if TYPE_CHECKING:
    from business_rule_engine.interfaces import Condition, Action, Rule


class RuleBuilder:

    def __init__(self, condition: Condition) -> None:
        self.__condition: Condition = condition

    @staticmethod
    def when(condition: Condition) -> RuleBuilder:
        return RuleBuilder(condition)

    def then(self, action: Action) -> Rule:
        return DefaultRule(
            condition=self.__condition,
            action=action
        )
