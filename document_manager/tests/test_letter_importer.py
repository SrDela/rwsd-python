from io import FileIO
from document_manager.classes.document import Document
from document_manager.classes.importer import LetterImporter
from document_manager.attributes import ADDRESS, BODY, PATIENT, TYPE, WIDTH, HEIGHT, PATH


class TestLetterImporter:

    importer: LetterImporter = LetterImporter()

    def test_should_import_letter_correctly(self):
        path: str = 'resources/letter1.letter'
        file_: FileIO = FileIO(path)
        document: Document = self.importer.import_file(file_)

        assert document.get_attribute(TYPE) == "LETTER"
        assert document.get_attribute(PATIENT) == "Joe Bloggs"
        assert document.get_attribute(ADDRESS) == "123 Fake Street\nWestminster\nLondon\nUnited Kingdom"
        assert document.get_attribute(BODY) == (
            "We are writing to you to confirm the re-scheduling of your appointment\n"
            "with Dr. Avaj from 29th December 2016 to 5th January 2017."
        )
