<!-- omit in toc -->
# VS Code Demo

This is a demo repository to show off the different features that I use in [VS code](https://code.visualstudio.com/).

- [Remote Development](#remote-development)
- [Python Development](#python-development)
  - [Jupyter Notebooks](#jupyter-notebooks)
  - [Interactive Python Interpreter](#interactive-python-interpreter)
  - [Interactive Debugging](#interactive-debugging)
  - [Testing](#testing)
- [R Development](#r-development)

## Remote Development

My favorite feature of VS code is remote development. This allows you to use a local install of VS code to edit code on a different computer (SSH), on Windows Subsystem for Linux (WSL), or in a docker container. When you use these extensions VS code starts a small server on the remote machine where it installs some of the extensions. Basically everything feels like you are working on the remote system. You have access to the file system and command line. Editing is async so you do not notice lag of working remotely.

## Python Development

Python support is probably second only to TypeScript. There is a team at Microsoft that is focused on improving python development so it is constantly improving. Python support is provided by the [Python Plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.python), but the new [Pylance Plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) will replace it in the future. I suggest install both right now.

### Jupyter Notebooks

Jupyter notebook are supported.

### Interactive Python Interpreter

### Interactive Debugging

### Testing

## R Development

