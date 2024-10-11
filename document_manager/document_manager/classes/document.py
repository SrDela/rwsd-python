from typing import Dict
from dataclasses import dataclass, field


@dataclass
class Document:
    attributes: Dict[str, str] = field(default_factory=dict())

    def get_attribute(self, attribute_name: str) -> str:
        return self.attributes.get(attribute_name, "")
