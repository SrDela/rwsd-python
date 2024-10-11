from io import FileIO
from document_manager.classes.document import Document
from document_manager.classes.importer import ReportImporter
from document_manager.attributes import BODY, PATIENT, TYPE


class TestReportImporter:

    importer: ReportImporter = ReportImporter()

    def test_should_import_report_correctly(self):
        path: str = 'resources/report1.report'
        file_: FileIO = FileIO(path)
        document: Document = self.importer.import_file(file_)

        assert document.get_attribute(TYPE) == "REPORT"
        assert document.get_attribute(PATIENT) == "Joe Bloggs"
        assert document.get_attribute(BODY) == (
            "On 5th January 2017 I examined Joe's teeth.\n"
            "We discussed his switch from drinking Coke to Diet Coke.\n"
            "No new problems were noted with his teeth."
        )
