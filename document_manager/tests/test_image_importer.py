from io import FileIO
from document_manager.classes.document import Document
from document_manager.classes.importer import ImageImporter
from document_manager.attributes import TYPE, WIDTH, HEIGHT, PATH


class TestImageImporter:

    importer: ImageImporter = ImageImporter()

    def test_should_import_image_correctly(self):
        path: str = 'resources/image.png'
        file_: FileIO = FileIO(path)
        document: Document = self.importer.import_file(file_)

        assert document.get_attribute(PATH) == path
        assert document.get_attribute(TYPE) == "IMAGE"
        assert document.get_attribute(WIDTH) == "280"
        assert document.get_attribute(HEIGHT) == "280"
