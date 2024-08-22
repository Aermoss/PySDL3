import setuptools, sys, os

from setuptools.dist import Distribution
from setuptools.command.install import install

class CustomInstall(install):
    def __init__(self, dist: Distribution) -> None:
        super(install, self).__init__(dist)
        
    def run(self) -> None:
        super(install, self).run()

        if sys.platform in ["win32"]:
            os.environ["PYSDL3_DISABLE_DOCS"] = "0"
            print("generating '__docs__.py'.", flush = True)
            sdl3 = __import__("sdl3")
            loaded = sum(len(v) for k, v in sdl3.functions.items())

            if loaded > 0:
                print(f"loaded {loaded} functions.", flush = True)

            else:
                print("something went wrong.", flush = True)

def main(argv):
    data = {
        "name": "PySDL3",
        "packages": ["sdl3", "sdl3.bin"],
        "version": "0.5.0a1",
        "description": "A pure Python wrapper for SDL3.",
        "long_description": open("README.md", "r", encoding = "utf-8").read(),
        "long_description_content_type": "text/markdown",
        "url": "https://github.com/Aermoss/PySDL3",
        "download_url": "https://pypi.python.org/pypi/PySDL3",
        "author": "Yusuf Rençber",
        "author_email": "aermoss.0@gmail.com",
        "license": "MIT",
        "include_package_data": True,
        "install_requires": [],
        "cmdclass": {"install": CustomInstall},
        "classifiers": [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ]
    }

    setuptools.setup(**data)

if __name__ == "__main__":
    sys.exit(main(sys.argv))