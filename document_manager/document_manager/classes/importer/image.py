from io import BytesIO, FileIO
from typing import Dict
from collections import namedtuple
from PIL.Image import open as load_image, Image
from document_manager.classes.document import Document
from document_manager.interfaces import Importer
from document_manager.attributes import HEIGHT, PATH, WIDTH, TYPE

ImageSize = namedtuple('ImageSize', ["width", "height"], defaults=["0", "0"])


class ImageImporter(Importer):

    def import_file(self, file_: FileIO) -> Document:
        attributes: Dict[str, str] = {}
        buffered_image: Image = load_image(BytesIO(file_.read()))
        attributes[PATH] = file_.name

        image_size: ImageSize = ImageSize(*buffered_image.size)
        attributes[WIDTH] = str(image_size.width)
        attributes[HEIGHT] = str(image_size.height)
        attributes[TYPE] = "IMAGE"

        return Document(attributes=attributes)
