from decimal import Decimal
from business_rule_engine.classes import Facts
from business_rule_engine.interfaces import Action, Stage


class ForecastAmount(Action):

    def execute(self, facts: Facts) -> None:
        deal_stage: Stage = Stage[facts.get_fact('stage')]
        amount: Decimal = Decimal(facts.get_fact('amount'))
        forecasted_amount: Decimal = amount * deal_stage.value
        facts.add_fact('forecasted_amount', str(forecasted_amount))
        print("Forecasted amount: ", forecasted_amount)
