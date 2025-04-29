# yarnlock

[![PyPI - Python Version](https://shields.monicz.dev/pypi/pyversions/yarnlock)](https://pypi.org/project/yarnlock)
[![Liberapay Patrons](https://shields.monicz.dev/liberapay/patrons/Zaczero?logo=liberapay&label=Patrons)](https://liberapay.com/Zaczero/)
[![GitHub Sponsors](https://shields.monicz.dev/github/sponsors/Zaczero?logo=github&label=Sponsors&color=%23db61a2)](https://github.com/sponsors/Zaczero)

Quickly parse yarn dependencies information into a Python dictionary. The output is typed using a TypedDict class, making it more convenient to work with.

## Installation

The recommended installation method is through the PyPI package manager. The project is implemented in Rust and several pre-built binary wheels are available for Linux, macOS, and Windows, with support for both x64 and ARM architectures.

```sh
pip install yarnlock
```

## Basic usage

```py
from pathlib import Path
from yarnlock import yarnlock_parse

yarnlock_parse(Path('yarn.lock').read_text())
# ->
# {
#     '@babel/cli': {
#         '^7.24.8': {
#         'dependencies': {
#             'glob': '^7.2.0',
#             'slash': '^2.0.0',
#             'make-dir': '^2.1.0',
#             'commander': '^6.2.0',
#             'convert-source-map': '^2.0.0',
#             'fs-readdir-recursive': '^1.1.0',
#             '@jridgewell/trace-mapping': '^0.3.25',
#         },
#         'optionalDependencies': {
#             'chokidar': '^3.4.0',
#             '@nicolo-ribaudo/chokidar-2': '2.1.8-no-fsevents.3',
#         },
#         'version': '7.24.8',
#         'resolved': 'https://registry.npmjs.org/@babel/cli/-/cli-7.24.8.tgz',
#         'integrity': 'sha512-isdp+G6DpRyKc+3Gqxy2rjzgF7Zj9K0mzLNnxz+E/fgeag8qT3vVulX4gY9dGO1q0y+0lUv6V3a+uhUzMzrwXg==',
#       },
#     },
#     ...
# }
```
