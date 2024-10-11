from typing import List
from business_rule_engine.classes import Facts, Inspector, Report
from business_rule_engine.interfaces import ConditionalAction
from actions import JobTitleCondition


class TestInspector:

    def test_inspect_one_condition_evaluates_true(self):
        facts: Facts = Facts()
        facts.add_fact('job_title', 'CEO')
        conditional_action: ConditionalAction = JobTitleCondition()
        inspector: Inspector = Inspector([conditional_action])
        report_list: List[Report] = inspector.inspect(facts)

        assert 1 == len(report_list)
        assert True == report_list[0].is_positive
