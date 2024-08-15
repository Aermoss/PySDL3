from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as file:
    description = file.read()

setup(
    name = "PySDL3",
    packages = ["sdl3"],
    version = "0.2.2a0",
    description = "A pure Python wrapper for SDL3.",
    long_description = description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Aermoss/PySDL3",
    author = "Yusuf Rençber",
    author_email = "aermoss.0@gmail.com",
    license = "MIT",
    include_package_data = True
)