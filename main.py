import argparse

from archive import ArchiveLeaf, ArchiveNode


def main(path):
    # build archive tree
    reddit_node = ArchiveNode("reddit")
    reddit_node.add_node(ArchiveLeaf("naerokeht", "redditpass"))

    github_node = ArchiveNode("github")
    github_node.add_node(ArchiveLeaf("changeemma", "githubpass"))

    gmail_node = ArchiveNode("gmail")
    gmail_node.add_node(ArchiveLeaf("changeemma@gmail.com", "gmpass1"))
    gmail_node.add_node(ArchiveLeaf("echang.dev@gmail.com", "gmpass2"))

    archive = ArchiveNode("archive")
    archive.add_node(reddit_node)
    archive.add_node(github_node)
    archive.add_node(gmail_node)

    # traverse archive
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
