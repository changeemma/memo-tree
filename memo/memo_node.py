from .memo_base import MemoBase


class MemoNode(MemoBase):
    def __init__(self, name: str):
        super().__init__(name)
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def browse(self, name: str) -> MemoBase:
        for node in self.nodes:
            if node.is_named(name):
                return node
        raise KeyError

    def open(self):
        print('\n'.join([str(n) for n in self.nodes]))
