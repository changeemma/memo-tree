import argparse

from memo import MemoLeaf, MemoNode


def main(path):
    # build memo tree
    reddit_node = MemoNode("reddit")
    reddit_node.add_node(MemoLeaf("naerokeht", "redditpass"))

    github_node = MemoNode("github")
    github_node.add_node(MemoLeaf("changeemma", "githubpass"))

    gmail_node = MemoNode("gmail")
    gmail_node.add_node(MemoLeaf("changeemma@gmail.com", "gmpass1"))
    gmail_node.add_node(MemoLeaf("echang.dev@gmail.com", "gmpass2"))

    archive = MemoNode("memo")
    archive.add_node(reddit_node)
    archive.add_node(github_node)
    archive.add_node(gmail_node)

    # traverse memo
    for p in path:
        archive = archive.browse(p)

    # open memo
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
