from io import FileIO
from typing import Dict
from document_manager.attributes import BODY, PATIENT, TYPE
from document_manager.classes.document import Document
from document_manager.classes.file.text import TextFile
from document_manager.interfaces import Importer


class ReportImporter(Importer):

    __NAME_PREFIX: str = "Patient: "

    def import_file(self, file_: FileIO) -> Document:
        text_file: TextFile = TextFile(file_)

        text_file.add_line_suffix(self.__NAME_PREFIX, PATIENT)
        text_file.add_lines(2, lambda _: False, BODY)

        attributes: Dict[str, str] = text_file.attributes
        attributes[TYPE] = "REPORT"
        return Document(attributes=attributes)
