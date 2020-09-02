<!-- omit in toc -->
# VS Code Demo

This is a demo repository to show off the different features that I use in [VS code](https://code.visualstudio.com/). This is meant to be an interactive demo so this readme is a little sparse.

- [Installation](#installation)
  - [On a Linux Host](#on-a-linux-host)
  - [Docker Container](#docker-container)
- [Resources](#resources)
- [Python Development](#python-development)
- [R Development](#r-development)

## Installation

### On a Linux Host

The `bootstrap.sh` script will create a conda repository in the project folder `./venv`.

### Docker Container

The Dockerfile is used to create a Docker container installing requirements into the `base` conda environment.

## Resources

VS Code's [documentation](https://code.visualstudio.com/docs) is really good with lots of examples.

## Python Development

Python support is probably second only to TypeScript. There is a team at Microsoft that is focused on improving python development so it is constantly improving. Python support is provided by the [Python Plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.python), but the new [Pylance Plugin](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) will replace it in the future. I suggest install both right now.

Topics discussed include:

- Interactive Python Interpreter and Jupyter Notebooks
- Interactive Debugging
- Testing

## R Development

My favorite feature of VS code is remote development. This allows you to use a local install of VS code to edit code on a different computer (SSH), on Windows Subsystem for Linux (WSL), or in a docker container. When you use these extensions VS code starts a small server on the remote machine where it installs some of the extensions. Basically everything feels like you are working on the remote system. You have access to the file system and command line. Editing is async so you do not notice lag of working remotely.

- Interactive R Interpreter
