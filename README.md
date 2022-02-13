# memo-tree
A cli tool to easily store and retrieve data in a tree-like data structure. It is designed to work with dmenu.

## Requirements
- a copy/paste mechanism to be used by [pyperclip](https://pypi.org/project/pyperclip/
) library. For Ubuntu, use `xsel`, do not use `xclip` (https://github.com/asweigart/pyperclip/issues/116)
- [dmenu](https://tools.suckless.org/dmenu/). For mac users, use [dmenu-mac](https://github.com/oNaiPs/dmenu-mac) but make sure that is available as dmenu before executing the script (i.e. `ln -s /usr/local/bin/dmenu-mac /usr/local/bin/dmenu`).

## TODO
- implement add-memo
- implement autocomplete (heads up for security issues)
- use an orm to persist data in db
