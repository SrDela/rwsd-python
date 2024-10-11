from io import FileIO
from document_manager.attributes import AMOUNT, BODY
from document_manager.classes.file import TextFile


class TestTextFile:

    def test_should_map_line_suffix_to_attribute_by_prefix(self):
        file_: FileIO = FileIO('resources/invoice1.invoice')
        text_file = TextFile(file_)
        text_file.add_line_suffix("Amount: ", AMOUNT)

        assert text_file.attributes[AMOUNT] == "$100"

    def test_should_map_lines_to_attribute_correctly(self):
        file_: FileIO = FileIO('resources/report1.report')
        text_file = TextFile(file_)
        text_file.add_lines(2, lambda _: False, BODY)

        assert text_file.attributes[BODY] == (
            "On 5th January 2017 I examined Joe's teeth.\n"
            "We discussed his switch from drinking Coke to Diet Coke.\n"
            "No new problems were noted with his teeth."
        )
