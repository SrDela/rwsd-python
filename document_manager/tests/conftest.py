from pytest import fixture

from document_manager.classes.system import DocumentManagementSystem


@fixture()
def system() -> DocumentManagementSystem:
    return DocumentManagementSystem()
