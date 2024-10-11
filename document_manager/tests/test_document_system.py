from typing import Iterator, List, Tuple
import pytest
from document_manager.attributes import ADDRESS, BODY, PATIENT, TYPE
from document_manager.classes.document import Document
from document_manager.classes.system import DocumentManagementSystem
from document_manager.exceptions.file import UnknownFileTypeException


class TestDocumentManagementSystem:

    def test_should_raise_exception_if_file_not_exists(self, system: DocumentManagementSystem):
        path: str = 'resources/notexists.ext'
        with pytest.raises(UnknownFileTypeException, match=f"No file found in: {path}"):
            system.import_file(path)

    def test_should_raise_exception_for_no_extension_file(self, system: DocumentManagementSystem):
        path: str = 'resources/no_ext'
        with pytest.raises(UnknownFileTypeException, match=f"No extension found for file: {path}"):
            system.import_file(path)

    def test_should_raise_exception_for_invalid_extension(self, system: DocumentManagementSystem):
        path: str = 'resources/invalid_file.txt'
        with pytest.raises(UnknownFileTypeException, match=f"For file: {path}"):
            system.import_file(path)

    def test_should_raise_exception_for_invalid_file(self, system: DocumentManagementSystem):
        path: str = 'resources/file.'
        with pytest.raises(UnknownFileTypeException, match=f"No extension found for file: {path}"):
            system.import_file(path)

    def test_file_is_imported_correctly(self, system: DocumentManagementSystem):
        path: str = 'resources/letter1.letter'
        system.import_file(path)
        contents: Tuple[Document] = system.contents()
        assert len(contents) == 1
        assert contents[0].get_attribute(TYPE) == "LETTER"
        assert contents[0].get_attribute(PATIENT) == "Joe Bloggs"
        assert contents[0].get_attribute(ADDRESS) == "123 Fake Street\nWestminster\nLondon\nUnited Kingdom"
        assert contents[0].get_attribute(BODY) == (
            "We are writing to you to confirm the re-scheduling of your appointment\n"
            "with Dr. Avaj from 29th December 2016 to 5th January 2017."
        )

    def test_files_are_imported_correctly(self, system: DocumentManagementSystem):
        path: str = 'resources/letter1.letter'
        system.import_file(path)

        path: str = 'resources/report1.report'
        system.import_file(path)
        contents: Tuple[Document] = system.contents()
        assert len(contents) == 2

        assert contents[0].get_attribute(TYPE) == "LETTER"
        assert contents[0].get_attribute(PATIENT) == "Joe Bloggs"
        assert contents[0].get_attribute(ADDRESS) == "123 Fake Street\nWestminster\nLondon\nUnited Kingdom"
        assert contents[0].get_attribute(BODY) == (
            "We are writing to you to confirm the re-scheduling of your appointment\n"
            "with Dr. Avaj from 29th December 2016 to 5th January 2017."
        )

        assert contents[1].get_attribute(TYPE) == "REPORT"
        assert contents[1].get_attribute(PATIENT) == "Joe Bloggs"
        assert contents[1].get_attribute(BODY) == (
            "On 5th January 2017 I examined Joe's teeth.\n"
            "We discussed his switch from drinking Coke to Diet Coke.\n"
            "No new problems were noted with his teeth."
        )

    def test_query_search_retrieves_correctly(self, system: DocumentManagementSystem):
        path: str = 'resources/letter1.letter'
        system.import_file(path)

        path: str = 'resources/report1.report'
        system.import_file(path)

        documents: Iterator[Document] = system.search("patient:Joe Bloggs")
        assert len(list(documents)) == 2

        documents: Iterator[Document] = system.search("patient:Joe Bloggs,type:REPORT,body:5th January 2017")
        document_list: List[Document] = list(documents)
        assert len(document_list) == 1
        assert document_list[0].get_attribute(BODY) == (
            "On 5th January 2017 I examined Joe's teeth.\n"
            "We discussed his switch from drinking Coke to Diet Coke.\n"
            "No new problems were noted with his teeth."
        )
