from document_manager.classes import Document
from document_manager.attributes import TYPE, AMOUNT


class TestDocument:

    document: Document = Document(attributes={
        TYPE: "LETTER",
        AMOUNT: "$200"
    })

    def test_should_return_correctly_attributes(self):
        assert self.document.get_attribute(TYPE) == "LETTER"
        assert self.document.get_attribute(AMOUNT) == "$200"

    def test_should_return_empty_for_non_existing_attribute(self):
        assert self.document.get_attribute("UNKNOWN") == ""
