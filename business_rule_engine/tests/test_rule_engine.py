from business_rule_engine import BusinessRuleEngine
from business_rule_engine.interfaces import Action, Stage
from business_rule_engine.classes import Facts, RuleBuilder
from conditions import Prospect
from actions import ForecastAmount
from unittest.mock import Mock


class TestRuleEngine:

    def test_should_have_no_rules_initially(self):
        facts: Facts = Facts()
        engine: BusinessRuleEngine = BusinessRuleEngine(facts)
        assert 0 == engine.count()

    def test_should_add_one_action(self):
        facts: Facts = Facts()
        engine: BusinessRuleEngine = BusinessRuleEngine(facts)
        engine.add_rule(RuleBuilder.when(Prospect.IsCEO()).then(ForecastAmount()))
        assert 1 == engine.count()

    def test_should_execute_one_action(self):
        facts: Facts = Facts()
        facts.add_fact('stage', Stage.LEAD.name)
        facts.add_fact('amount', "1000")
        facts.add_fact('job_title', 'CEO')
        engine: BusinessRuleEngine = BusinessRuleEngine(facts)
        MockedForecastAmount: Action = Mock(ForecastAmount())

        engine.add_rule(RuleBuilder.when(Prospect.IsCEO()).then(MockedForecastAmount))
        engine.run()

        MockedForecastAmount.execute.assert_called_once_with(facts)

    def test_should_not_execute_action(self):
        facts: Facts = Facts()
        facts.add_fact('job_title', 'Analyst')
        engine: BusinessRuleEngine = BusinessRuleEngine(facts)
        MockedForecastAmount: Action = Mock(ForecastAmount())

        engine.add_rule(RuleBuilder.when(Prospect.IsCEO()).then(MockedForecastAmount))
        engine.run()

        MockedForecastAmount.execute.assert_not_called()
