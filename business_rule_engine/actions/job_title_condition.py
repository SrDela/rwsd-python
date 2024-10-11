from business_rule_engine.interfaces import ConditionalAction
from business_rule_engine.classes import Facts


class JobTitleCondition(ConditionalAction):

    def evaluate(self, facts: Facts) -> bool:
        return "CEO" == facts.get_fact('job_title')

    def perform(self, facts: Facts) -> None:
        return super().perform(facts)
