from __future__ import annotations
from typing import TYPE_CHECKING

from .facts import Facts

if TYPE_CHECKING:
    from business_rule_engine.interfaces import ConditionalAction


class Report:

    def __init__(
        self,
        facts: Facts,
        conditional_action: ConditionalAction,
        is_positive: bool
    ) -> None:
        self.__facts: Facts = facts
        self.__conditional_action: ConditionalAction = conditional_action
        self.__is_positive: bool = is_positive

    @property
    def conditional_action(self) -> ConditionalAction:
        return self.__conditional_action

    @property
    def facts(self) -> Facts:
        return self.__facts

    @property
    def is_positive(self) -> bool:
        return self.__is_positive

    def __str__(self) -> str:
        return (
            "Report<"
            f"conditional_action={self.__conditional_action}, "
            f"facts={self.__facts}, "
            f"result={self.__is_positive}"
            ">"
        )
