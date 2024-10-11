from __future__ import annotations
from typing import List, TYPE_CHECKING
from .classes import Facts

if TYPE_CHECKING:
    from .interfaces import Rule


class BusinessRuleEngine:

    def __init__(self, facts: Facts) -> None:
        self.__facts: Facts = facts
        self.__rules: List[Rule] = []

    def add_rule(self, rule: Rule) -> None:
        self.__rules.append(rule)

    def count(self) -> int:
        return len(self.__rules)

    def run(self) -> None:
        for rule in self.__rules:
            rule.perform(self.__facts)
        return
