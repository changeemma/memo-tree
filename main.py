import argparse
import pyperclip


DATA = {
    "reddit": {"naerokeht": "redditpass"},
    "github": {"changeemma": "ghpass"},
    "gmail": {
        "changeemma@gmail.com": "gmpass",
        "echang.dev@gmail.com": "fipass",
    }
}


def main(options):
    archive = DATA
    for opt in options:
        archive = archive[opt]

    if isinstance(archive, dict):
        print('\n'.join(archive.keys()))
    else:
        pyperclip.copy(archive)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a description.')
    parser.add_argument('options',
                        metavar='node',
                        type=str,
                        nargs='*',
                        help='this is help')
    args = parser.parse_args()
    main(args.options)
