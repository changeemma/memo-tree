from .memo_base import MemoBase


class MemoNode(MemoBase):
    def __init__(self, name: str):
        super().__init__(name)
        self.nodes = []

    def browse(self, name: str) -> MemoBase:
        for node in self.nodes:
            if node.is_named(name):
                return node
        raise KeyError

    def has_node(self, name: str) -> bool:
        try:
            _ = self.browse(name)
        except KeyError:
            return False
        return True

    def add_node(self, node: MemoBase) -> None:
        self.nodes.append(node)

    def open(self) -> None:
        nodes = '\n'.join(n.print() for n in self.nodes)
        print(nodes)
