import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "temp")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

os.environ["SDL_DOC_GENERATOR"] = "0"
os.environ["SDL_CTYPES_ALIAS_FIX"] = "1"
os.environ["SDL_DISABLE_METADATA"] = "1"
os.environ["SDL_PLATFORM_AGNOSTIC"] = "1"
os.environ["SDL_IGNORE_MISSING_FUNCTIONS"] = "1"
os.environ["SDL_CHECK_BINARY_VERSION"] = "0"
os.environ["SDL_DOWNLOAD_BINARIES"] = "0"
os.environ["SDL_FIND_BINARIES"] = "0"
os.makedirs("temp", exist_ok = True)

import sdl3

for i in list(sdl3.SDL_BINARY_VAR_MAP_INV.keys()):
    with open(f"temp/{i}.py", "w") as file:
        file.write(sdl3.SDL_GENERATE_DOCS([i], rst = True))

project = "PySDL3"
copyright = "2025, Yusuf Rençber"
author = "Yusuf Rençber"
release = sdl3.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo"
]

templates_path = []
exclude_patterns = ["build"]

language = "en"
pygments_style = None

html_theme = "sphinx_rtd_theme"
html_static_path = []