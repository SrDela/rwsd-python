from io import FileIO, StringIO
from typing import Callable, Dict, Tuple
from document_manager.attributes import PATH


class TextFile:

    def __init__(self, file_: FileIO) -> None:
        self.__attributes: Dict[str, str] = {}
        self.__attributes[PATH] = file_.name
        self.__lines: Tuple[str] = tuple(map(bytes.decode, file_.readlines()))

    @property
    def attributes(self) -> Dict[str, str]:
        return self.__attributes

    def add_lines(
        self,
        start: int,
        is_end: Callable[[str], bool],
        attribute_name: str
    ) -> int:
        line_builder: StringIO = StringIO("")
        last_visited_idx: int = start
        lines: Tuple[str] = tuple(self.__lines)
        for idx in range(start, len(lines)):
            last_visited_idx = idx
            line = lines[idx].strip()
            if is_end(line):
                break
            line_builder.write(line)
            line_builder.write("\n")
        self.__attributes[attribute_name] = line_builder.getvalue().strip()
        return last_visited_idx

    def add_line_suffix(self, prefix: str, attribute_name: str) -> None:
        for line in self.__lines:
            if line.startswith(prefix):
                self.__attributes[attribute_name] = line[len(prefix):].strip()
                break
        return
