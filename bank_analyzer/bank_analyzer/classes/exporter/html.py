from io import StringIO

from bank_analyzer.interfaces.exporter import Exporter

from bank_analyzer.classes.summary import SummaryStatistics


class HTMLExporter(Exporter):

    def export(self, summary_statistics: SummaryStatistics) -> str:
        result: StringIO = StringIO("<!doctype html>")
        result.write("<html lang='en'>")
        result.write("<head><title>Bank Transaction Report </title></head>")
        result.write("<body>")
        result.write("<ul>")
        result.write(f"<li><strong>The sum is</strong>{round(summary_statistics.sum_, 2)}</li>")
        result.write(f"<li><strong>The average is</strong>{round(summary_statistics.average, 2)}</li>")
        result.write(f"<li><strong>The max is</strong>{round(summary_statistics.max_, 2)}</li>")
        result.write(f"<li><strong>The min is</strong>{round(summary_statistics.min_, 2)}</li>")
        result.write("</ul>")
        result.write("</body>")
        result.write("</html>")
        return result.getvalue()