from setuptools import setup

with open("README.md", "r", encoding = "UTF-8") as file:
    description = file.read()

setup(
    name = "PySDL3",
    packages = ["sdl3"],
    version = "0.1.1a0",
    description = description.split("\n")[1],
    long_description = description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Aermoss/PySDL3",
    author = "Yusuf Rençber",
    author_email = "aermoss.0@gmail.com",
    license = "MIT",
    include_package_data = True
)