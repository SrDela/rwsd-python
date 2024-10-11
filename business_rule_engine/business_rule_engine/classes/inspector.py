from __future__ import annotations
from typing import List, TYPE_CHECKING

from .facts import Facts
from .report import Report

if TYPE_CHECKING:
    from business_rule_engine.interfaces import ConditionalAction


class Inspector:

    def __init__(self, conditional_action_list: List[ConditionalAction]) -> None:
        self.__conditional_action_list: List[ConditionalAction] = conditional_action_list

    def inspect(self, facts: Facts) -> List[Report]:
        report_list: List[Report] = []
        for conditional_action in self.__conditional_action_list:
            condition_result: bool = conditional_action.evaluate(facts)
            report_list.append(
                Report(
                    facts=facts,
                    conditional_action=conditional_action,
                    is_positive=condition_result
                )
            )
        return report_list
