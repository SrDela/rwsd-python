from __future__ import annotations
from typing import Dict
from document_manager.classes import Document


class Query:

    def __init__(self, clauses: Dict[str, str]) -> None:
        self.__clauses: Dict[str, str] = clauses

    @classmethod
    def parse(cls, query: str) -> Query:
        parsed_clauses: Dict[str, str] = {}
        for clause in query.split(','):
            key, value = clause.split(":", 1)
            parsed_clauses[key] = value
        return Query(parsed_clauses)

    def test(self, document: Document) -> bool:
        for key, clause_value in self.__clauses.items():
            document_value = document.attributes.get(key)
            if document_value is None or document_value.find(clause_value) == -1:
                return False
        return True
