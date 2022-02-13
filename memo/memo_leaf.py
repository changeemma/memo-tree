import pyperclip

from .memo_base import MemoBase


class MemoLeaf(MemoBase):
    def __init__(self, name: str, content: str):
        super().__init__(name)
        self.content = content

    def browse(self, name) -> MemoBase:
        raise KeyError

    def open(self) -> None:
        pyperclip.copy(self.content)
