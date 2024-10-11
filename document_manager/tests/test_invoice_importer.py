from io import FileIO
from document_manager.classes.document import Document
from document_manager.classes.importer import InvoiceImporter
from document_manager.attributes import AMOUNT, BODY, PATIENT, TYPE


class TestInvoiceImporter:

    importer: InvoiceImporter = InvoiceImporter()

    def test_should_import_report_correctly(self):
        path: str = 'resources/invoice1.invoice'
        file_: FileIO = FileIO(path)
        document: Document = self.importer.import_file(file_)

        assert document.get_attribute(TYPE) == "INVOICE"
        assert document.get_attribute(PATIENT) == "Joe Bloggs"
        assert document.get_attribute(AMOUNT) == "$100"
