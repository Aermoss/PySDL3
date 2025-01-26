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
If you want to use your own binaries, you can simply place them in the "sdl3/bin" directory (the default binary path)
or you can use the path you’ve specified with the ``SDL_BINARY_PATH`` environment variable **before importing PySDL3**, as follows: ::

  import os

  os.environ["SDL_BINARY_PATH"] = "/path/to/your/binaries"

  import sdl3

  ...

PySDL3 will automatically detect the binaries in the given path and use them instead of downloading new ones.
However, **if it detects that even a single binary is missing, it will download new binaries and overwrite the existing ones.**
You can disable this behavior by setting the ``SDL_DOWNLOAD_BINARIES`` environment variable to "0"
but still make sure you have all 6 binaries installed, **otherwise it will not work**.

If there are other files you want to keep in the binary path, you can disable the warning message by setting the ``SDL_IGNORE_REDUNDANT_FILES`` environment variable to "1".

If the versions of your binaries are different from the implementation version of PySDL3, you can disable the warning messages by setting the ``SDL_CHECK_BINARY_VERSION``
environment variable to "0" but **be aware that using an older binary version may cause unexpected behavior**.

.. _PyPI: https://pypi.org/project/PySDL3
.. _GitHub: https://github.com/Aermoss/PySDL3