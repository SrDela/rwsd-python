from typing import Iterator
from json import dumps
from document_manager.classes.document import Document
from document_manager.classes.system import DocumentManagementSystem


class MainApplication:

    def __init__(self) -> None:
        self.__document_manager: DocumentManagementSystem = DocumentManagementSystem()

    def load_files(self, *files: str) -> None:
        for file_ in files:
            self.__document_manager.import_file(file_)

    def run(self) -> None:
        results: Iterator[Document] = self.__document_manager.search("type:INVOICE,amount:$100")
        for result in results:
            print(dumps(result.attributes, indent=4))


if __name__ == "__main__":
    app = MainApplication()
    app.load_files(
        "resources/image.png",
        "resources/letter1.letter",
        "resources/report1.report",
        "resources/invoice1.invoice",
    )
    app.run()
