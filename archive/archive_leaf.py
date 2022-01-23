import pyperclip

from .archive_base import ArchiveBase


class ArchiveLeaf(ArchiveBase):
    def __init__(self, name: str, content: str):
        super().__init__(name)
        self.content = content

    def browse(self, name) -> ArchiveBase:
        raise KeyError

    def open(self) -> None:
        pyperclip.copy(self.content)