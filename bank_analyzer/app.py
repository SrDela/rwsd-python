from bank_analyzer.classes.bank_statement_analyzer import BankStatementAnalyzer
from bank_analyzer.classes.exporter import HTMLExporter
from bank_analyzer.classes.parser import BankStatementCSVParser
from bank_analyzer.interfaces import BankStatementParser, Exporter


class MainApplication:

    def __init__(self):
        self.__statement_analyzer: BankStatementAnalyzer = BankStatementAnalyzer()
        self.__statement_parser: BankStatementParser = BankStatementCSVParser()
        self.__exporter: Exporter = HTMLExporter()

    def run(self):
        self.__statement_analyzer.analyze("resources/statements.csv", self.__statement_parser, self.__exporter)


if __name__ == "__main__":
    app = MainApplication()
    app.run()
