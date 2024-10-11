from business_rule_engine.interfaces import Condition
from business_rule_engine.classes import Facts


class IsCEO(Condition):

    def evaluate(self, facts: Facts) -> bool:
        return 'CEO' == facts.get_fact('job_title')
