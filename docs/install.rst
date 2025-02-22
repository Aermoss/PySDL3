Installing PySDL3
=================
This page shows how to install PySDL3 and how to use your own binaries with it.

From PyPI
---------
You can download the latest stable version of PySDL3 from PyPI_ using the following command: ::

  pip install --upgrade PySDL3

*Please note that PySDL3 may not yet be available for your platform, please read the prerequisites section below.*

From GitHub
-----------
You can download the latest development version of PySDL3 from GitHub_ with the following command: ::

  pip install --upgrade git+https://github.com/Aermoss/PySDL3.git

*Please note that downloading the latest development version may cause PySDL3 to have unexpected bugs.*

Prerequisites
-------------
For PySDL3 to run properly, you must be using at least **Python 3.10** and one of the following platforms:

* **Linux** (AMD64, ARM64)
* **Windows** (AMD64, ARM64)
* **Darwin** (AMD64, ARM64)

PySDL3 will download all the necessary binaries for you on the first run, if you want to use your own binaries read the following section.

Custom Binaries
---------------
There are two methods to use your own binaries with PySDL3, the metadata method and the environment variable method.

.. highlight:: json

The Metadata Method
~~~~~~~~~~~~~~~~~~~
The metadata method was developed to allow PySDL3 to automatically download and manage its own binaries.
To use this method, you need to create a file named ``metadata.json`` in the binary path, as follows: ::

  {
    "system": "Darwin",
    "arch": "ARM64",
    "target": "v0.9.4b5",
    "files": [
      "./libSDL3.dylib",
      "./libSDL3_image.dylib",
      "./libSDL3_mixer.dylib",
      "./libSDL3_ttf.dylib"
    ],
    "repair": true,
    "find": true
  }

The ``files`` list must contain the names of the binaries **you want to use** and the ``system`` and ``arch`` fields must match your platform.
The ``repair`` field allows files to be downloaded if they are missing (with ``SDL_DOWNLOAD_BINARIES``, enabled by default), and the ``find`` field allows
missing files to be searched in the system libraries (with ``SDL_FIND_BINARIES``, enabled by default), ``files`` list can be empty while using ``find`` feature.
The ``target`` field is optional and can be used to specify the target PySDL3 version for the binaries.

PySDL3 will automatically start downloading new binaries if the current version is higher from the specified target version or
if it cannot find the ``metadata.json`` file **or the binaries specified by it** (when repair enabled) in the binary path ("sdl3/bin" by default).

*Please note that PySDL3 will download all 6 binaries (when repair mode enabled) and overwrite any existing ones.*

You can disable this behavior also by setting the ``SDL_DOWNLOAD_BINARIES`` environment variable to "0"
but still make sure you have all binaries specified in the ``metadata.json`` file installed, otherwise some modules will be disabled.

.. highlight:: python

The Environment Variable Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The environment variable method is the easiest and recommended way to use your own binaries with PySDL3.
In order to use this method, you just need to set ``SDL_DISABLE_METADATA`` to "1" as follows: ::

  import os

  os.environ["SDL_DISABLE_METADATA"] = "1" # Disable metadata method, "0" by default.
  os.environ["SDL_BINARY_PATH"] = "/path/to/your/binaries" # Set the path to your binaries, "sdl3/bin" by default.
  os.environ["SDL_CHECK_BINARY_VERSION"] = "0" # Disable binary version checking, "1" by default.
  os.environ["SDL_IGNORE_MISSING_FUNCTIONS"] = "1" # Disable missing function warnings, "0" by default.
  os.environ["SDL_FIND_BINARIES"] = "1" # Search for binaries in the system libraries, "1" by default.

  import sdl3

  ...

PySDL3 will search for the binaries in the binary path and (if ``SDL_FIND_BINARIES`` is set to "1") in the system libraries.
If a binary is missing, the corresponding module will be automatically disabled (binaries will not be downloaded automatically in this method).

*Please note that using an older binary version may cause unexpected behavior.*

.. _PyPI: https://pypi.org/project/PySDL3
.. _GitHub: https://github.com/Aermoss/PySDL3