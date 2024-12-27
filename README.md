# Project Name

A brief description of your project: its purpose, main functionality, and usage.

## Requirements

Before starting with this project, ensure the following components are installed:

- Python 3.11.7 (CPython)
- Virtualenv 20.24.5
- MSYS2 (msys64) for working with DLL libraries

### Setting Up MSYS2

To work with the project, you need to have MSYS2 installed and configured with the following setup:

- The `ucrt64` environment is used for Python.
- Path to MSYS2: `C:\msys64\ucrt64`.

You can download MSYS2 from the [official website](https://www.msys2.org/). After installation, activate the `ucrt64` environment by running the following commands in the MSYS2 Shell:

```bash
$ pacman -Syu
$ pacman -S base-devel python python-pip
```


```bash
g++ -shared -o maze_lib.dll generator.cpp
```