from business_rule_engine.business_rule_engine import BusinessRuleEngine
from business_rule_engine.classes import Facts, RuleBuilder
from business_rule_engine.interfaces import Stage
from actions import ForecastAmount
from conditions import Prospect


class MainApplication:

    def __init__(self) -> None:
        self.__facts: Facts = Facts()
        self.__facts.add_fact('stage', Stage.LEAD.name)
        self.__facts.add_fact('amount', "1000")
        self.__facts.add_fact('job_title', 'CEO')
        self.__engine: BusinessRuleEngine = BusinessRuleEngine(self.__facts)

    def run(self) -> None:
        self.__engine.add_rule(RuleBuilder.when(Prospect.IsCEO()).then(ForecastAmount()))
        self.__engine.run()


if __name__ == "__main__":
    app = MainApplication()
    app.run()
