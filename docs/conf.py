import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sdl3

project = "PySDL3"
copyright = "2025, Yusuf Rençber"
author = "Yusuf Rençber"
release = sdl3.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.inheritance_diagram"
]

templates_path = []
exclude_patterns = ["_build"]

language = "en"
pygments_style = None

html_theme = "sphinx_rtd_theme"
html_static_path = []