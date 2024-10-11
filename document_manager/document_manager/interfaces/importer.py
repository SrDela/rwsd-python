from abc import ABC, abstractmethod
from io import FileIO
from document_manager.classes import Document


class Importer(ABC):

    @abstractmethod
    def import_file(self, file_: FileIO) -> Document:
        raise NotImplementedError
