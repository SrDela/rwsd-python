from bank_analyzer.classes.exporter import HTMLExporter
from bank_analyzer.classes.summary import SummaryStatistics
from decimal import Decimal
from bank_analyzer.classes.parser.html import MyHTMLParser


class TestHTMLExporter:

    exporter: HTMLExporter = HTMLExporter()

    def test_exports_valid_html(self):
        summary = SummaryStatistics(
            sum_=Decimal(100),
            max_=Decimal(30),
            min_=Decimal(-10),
            average=Decimal(300)
        )

        parser: MyHTMLParser = MyHTMLParser()
        parser.feed(self.exporter.export(summary))
        assert parser.is_text_html()
