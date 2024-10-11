from io import FileIO
from typing import Iterator, List, Dict, Tuple

from .query import Query
from .document import Document
from document_manager.interfaces import Importer
from document_manager.exceptions import UnknownFileTypeException
from document_manager.classes.importer import (
    LetterImporter, ReportImporter,
    ImageImporter, InvoiceImporter
)


class DocumentManagementSystem:

    def __init__(self) -> None:
        self.__documents: List[Document] = []
        self.__extension_to_importer: Dict[str, Importer] = {
            "letter": LetterImporter(),
            "report": ReportImporter(),
            "jpg": ImageImporter(),
            "png": ImageImporter(),
            "invoice": InvoiceImporter()
        }

    def import_file(self, path: str) -> None:

        try:
            file_: FileIO = FileIO(path)
        except FileNotFoundError:
            raise UnknownFileTypeException(f"No file found in: {path}")

        separator_idx: int = path.rfind('.')

        if separator_idx == -1:
            raise UnknownFileTypeException(
                f"No extension found for file: {path}"
            )

        if separator_idx == len(path) - 1:
            raise UnknownFileTypeException(
                f"No extension found for file: {path}"
            )

        extension: str = path[(separator_idx + 1):]
        importer: Importer = self.__extension_to_importer.get(extension)
        if importer is None:
            raise UnknownFileTypeException(f"For file: {path}")

        document: Document = importer.import_file(file_)
        self.__documents.append(document)

    def contents(self) -> Tuple[Document]:
        return tuple(self.__documents)

    def search(self, query: str) -> Iterator[Document]:
        return filter(Query.parse(query).test, self.__documents)
