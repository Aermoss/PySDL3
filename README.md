# PySDL3

[![Logo](https://github.com/Aermoss/PySDL3/blob/main/res/logo.png?raw=true)](https://github.com/Aermoss/PySDL3)

[![Tests](https://github.com/Aermoss/PySDL3/actions/workflows/run_tests.yml/badge.svg)](https://github.com/Aermoss/PySDL3/actions/workflows/run_tests.yml)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/PySDL3)](https://pypi.org/project/PySDL3)
[![PyPI Version](https://img.shields.io/pypi/v/PySDL3.svg)](https://pypi.org/project/PySDL3)
[![PyPI Downloads](https://img.shields.io/pypi/dm/PySDL3.svg)](https://pypi.org/project/PySDL3)
[![PyPI Status](https://img.shields.io/pypi/status/PySDL3.svg)](https://pypi.org/project/PySDL3)

PySDL3 is a pure Python wrapper around the SDL3, SDL3\_image, SDL3\_mixer, SDL3\_ttf, SDL3\_rtf, SDL3\_net and SDL3\_shadercross libraries.
It uses the built-in ctypes library to interface with SDL3 while providing an **understandable** function definition with docstrings, argument names and type hints, like this:

[![Screenshot](https://github.com/Aermoss/PySDL3/blob/main/res/snippet.png?raw=true)](https://github.com/Aermoss/PySDL3/blob/main/gpu.py)

## Getting Started
Just run one of the following commands in a terminal:
```bash
# To install the latest stable version from PyPI:
pip install --upgrade PySDL3

# To install the latest development version from GitHub:
pip install --upgrade git+https://github.com/Aermoss/PySDL3.git
```

## Requirements
There are no additional requirements since PySDL3 will download all the necessary binaries for you on the first run.

*SDL3 binaries will be downloaded from [PySDL3-Build](https://github.com/Aermoss/PySDL3-Build) repository, if you want to use your own binaries please read the [documentation](https://pysdl3.readthedocs.io/en/latest/install.html#custom-binaries).*

### Supported Platforms:
* **Linux** (AMD64, ARM64)
* **Windows** (AMD64, ARM64)
* **Darwin** (AMD64, ARM64)

## Documentation
The [documentation of PySDL3](https://pysdl3.readthedocs.io) can be found at: https://pysdl3.readthedocs.io.

*If you can't find what you are looking for there, it is highly recommended to look at the [official documentation of SDL3](https://wiki.libsdl.org/SDL3) since everything is defined exactly the same.*

## License
PySDL3 is available under the MIT license, see the [LICENSE](https://github.com/Aermoss/PySDL3/blob/main/LICENSE) file for more information.