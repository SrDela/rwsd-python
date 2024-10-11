from json import dumps, JSONEncoder
from decimal import Decimal

from bank_analyzer.interfaces.exporter import Exporter

from bank_analyzer.classes.summary import SummaryStatistics


class DecimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)


class JSONExporter(Exporter):

    def export(self, summary_statistics: SummaryStatistics) -> str:
        result: dict = summary_statistics.asdict()
        return dumps(result, cls=DecimalEncoder)
