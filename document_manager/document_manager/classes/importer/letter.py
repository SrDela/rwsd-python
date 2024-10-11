from io import FileIO
from typing import Dict
from document_manager.attributes import ADDRESS, BODY, PATIENT, TYPE
from document_manager.classes.document import Document
from document_manager.classes.file.text import TextFile
from document_manager.interfaces import Importer


class LetterImporter(Importer):

    __NAME_PREFIX: str = "Dear "

    def import_file(self, file_: FileIO) -> Document:
        text_file: TextFile = TextFile(file_)

        text_file.add_line_suffix(self.__NAME_PREFIX, PATIENT)

        line_num: int = text_file.add_lines(2, lambda line: line == "", ADDRESS)
        text_file.add_lines((line_num + 1), lambda line: line.startswith("regards,"), BODY)

        attributes: Dict[str, str] = text_file.attributes
        attributes[TYPE] = "LETTER"
        return Document(attributes=attributes)
