from io import FileIO
from typing import Dict
from document_manager.attributes import AMOUNT, PATIENT, TYPE
from document_manager.classes.document import Document
from document_manager.classes.file.text import TextFile
from document_manager.interfaces import Importer


class InvoiceImporter(Importer):

    __NAME_PREFIX: str = "Dear "
    __AMOUNT_PREFIX: str = "Amount: "

    def import_file(self, file_: FileIO) -> Document:
        text_file: TextFile = TextFile(file_)

        text_file.add_line_suffix(self.__NAME_PREFIX, PATIENT)
        text_file.add_line_suffix(self.__AMOUNT_PREFIX, AMOUNT)

        attributes: Dict[str, str] = text_file.attributes
        attributes[TYPE] = "INVOICE"
        return Document(attributes=attributes)
