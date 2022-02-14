import argparse
from typing import List

from memo import MemoLeaf, MemoNode


def main(path: List, file: str = ""):
    # build memo tree
    memo_tree = build_memo_tree(file)

    # traverse tree
    for p in path:
        memo_tree = memo_tree.browse(p)

    # open memo
    memo_tree.open()


def build_memo_tree(file: str):
    with open(file) as f:
        content = f.read().splitlines()

    root = MemoNode("memo")

    for line in content:
        path = line.split(',')
        content = path.pop()
        name = path.pop()
        leaf = MemoLeaf(name, content)

        node = root
        for p in path:
            if node.has_node(p) is False:
                node.add_node(MemoNode(p))
            node = node.browse(p)
        node.add_node(leaf)

    return root


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a description.')
    parser.add_argument('path',
                        metavar='node',
                        type=str,
                        nargs='*',
                        help='Path of nodes.')
    parser.add_argument('-f', '--file',
                        type=str,
                        help="CSV dump file.")
    args = parser.parse_args()
    main(args.path, args.file)
