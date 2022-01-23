import argparse
import pyperclip


class ArchiveTree:
    def __init__(self, name: str):
        self.name = name
        self.nodes = []

    def __str__(self):
        return self.name

    def add_node(self, node):
        self.nodes.append(node)

    def is_named(self, name: str):
        return self.name == name

    def browse(self, name: str):
        for node in self.nodes:
            if node.is_named(name):
                return node
        raise KeyError

    def open(self):
        print('\n'.join([str(n) for n in self.nodes]))


class ArchiveLeaf:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

    def __str__(self):
        return self.name

    def is_named(self, name: str):
        return self.name == name

    def browse(self, name):
        return self

    def open(self):
        pyperclip.copy(self.content)


reddit_node = ArchiveTree("reddit")
reddit_node.add_node(ArchiveLeaf("naerokeht", "redditpass"))

github_node = ArchiveTree("github")
github_node.add_node(ArchiveLeaf("changeemma", "githubpass"))

gmail_node = ArchiveTree("gmail")
gmail_node.add_node(ArchiveLeaf("changeemma@gmail.com", "gmpass1"))
gmail_node.add_node(ArchiveLeaf("echang.dev@gmail.com", "gmpass2"))

ARCHIVE = ArchiveTree("archive")
ARCHIVE.add_node(reddit_node)
ARCHIVE.add_node(github_node)
ARCHIVE.add_node(gmail_node)


def main(path):
    # traverse archive
    archive = ARCHIVE
    for p in path:
        archive = archive.browse(p)

    # open archive
    archive.open()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a description.')
    parser.add_argument('path',
                        metavar='node',
                        type=str,
                        nargs='*',
                        help='this is help')
    args = parser.parse_args()
    main(args.path)
