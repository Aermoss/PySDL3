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
.. highlight:: json

To use your own binaries, you need to create a file named ``metadata.json`` in the binary path, as follows: ::

  {
    "system": "Darwin",
    "arch": "ARM64",
    "target": "v0.9.4b4",
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

PySDL3 will automatically start downloading new binaries if the current version is higher from the specified target version
or if it cannot find the ``metadata.json`` file **or the binaries specified by it** (when repair enabled) in the binary path ("sdl3/bin" by default).

.. highlight:: python

You can set your own binary path with the ``SDL_BINARY_PATH`` environment variable **before importing PySDL3**, as follows: ::

  import os

  os.environ["SDL_BINARY_PATH"] = "/path/to/your/binaries"

  import sdl3

  ...

*Please note that PySDL3 will download all 6 binaries (when repair mode enabled) and overwrite any existing ones.*

You can also disable this behavior by setting the ``SDL_DOWNLOAD_BINARIES`` environment variable to "0"
but still make sure you have all binaries specified in the ``metadata.json`` file installed.

If the versions of your binaries are different from the implementation version of PySDL3, you can disable the warning messages by setting the ``SDL_CHECK_BINARY_VERSION``
environment variable to "0" but **be aware that using an older binary version may cause unexpected behavior**.

If you want to disable warning messages for missing binaries and/or functions,
you can set the ``SDL_IGNORE_MISSING_BINARIES`` and/or ``SDL_IGNORE_MISSING_FUNCTIONS`` environment variable(s) to "1".

.. _PyPI: https://pypi.org/project/PySDL3
.. _GitHub: https://github.com/Aermoss/PySDL3