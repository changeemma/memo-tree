# py-archive
A cli tool to easily store and retrieve data in a tree-like data structure. It is designed to work with dmenu

## Requirements
- a copy/paste mechanism to be used by [pyperclip](https://pypi.org/project/pyperclip/
) library. For Ubuntu, use `xsel`, do not use `xclip` (https://github.com/asweigart/pyperclip/issues/116)
- [dmenu](https://tools.suckless.org/dmenu/)

## TODO
- implement py-archive-add
- implement autocomplete (heads up for security issues)
- use an orm to persist data in db
