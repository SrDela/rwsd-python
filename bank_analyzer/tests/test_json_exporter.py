import pytest
from decimal import Decimal
from json import loads, JSONDecodeError
from bank_analyzer.classes.exporter import JSONExporter
from bank_analyzer.classes.summary import SummaryStatistics


class TestJSONExporter:

    exporter: JSONExporter = JSONExporter()

    def test_exports_valid_json(self):
        summary = SummaryStatistics(
            sum_=Decimal(100),
            max_=Decimal(30),
            min_=Decimal(-10),
            average=Decimal(300)
        )

        result = self.exporter.export(summary)
        try:
            valid_json = loads(result)
            assert Decimal(valid_json['sum_']) == summary.sum_
            assert Decimal(valid_json['max_']) == summary.max_
            assert Decimal(valid_json['min_']) == summary.min_
            assert Decimal(valid_json['average']) == summary.average
        except JSONDecodeError:
            pytest.fail("Invalid json.")
