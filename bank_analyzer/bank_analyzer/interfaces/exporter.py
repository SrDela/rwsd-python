from abc import ABC, abstractmethod

from bank_analyzer.classes.summary import SummaryStatistics


class Exporter(ABC):

    @abstractmethod
    def export(self, summary_statistics: SummaryStatistics) -> str:
        raise NotImplementedError
