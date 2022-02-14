# memo-tree
memo-tree is a tool that helps you to remember stuff.
access to data stored in a tree-like structure and copies it into your clipboard.
it is designed to work with dmenu.

## Requirements
- a copy/paste mechanism to be used by [pyperclip](https://pypi.org/project/pyperclip/
) library. For Ubuntu, use `xsel`, do not use `xclip` (https://github.com/asweigart/pyperclip/issues/116)
- [dmenu](https://tools.suckless.org/dmenu/). For mac users, use [dmenu-mac](https://github.com/oNaiPs/dmenu-mac) but make sure that is available as dmenu before executing the script (i.e. `ln -s /usr/local/bin/dmenu-mac /usr/local/bin/dmenu`).

## Install (Ubuntu)
```bash
$ pip3 install -r requirements.txt
$ sudo ln -s $(pwd)/run.sh /usr/local/bin/memo-tree
```


## TODO
- persist data in db
