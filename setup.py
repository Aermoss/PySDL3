import setuptools, sys, os

from setuptools.dist import Distribution
from setuptools.command.install import install

class CustomInstall(install):
    def __init__(self, dist: Distribution) -> None:
        super(install, self).__init__(dist)
        
    def run(self) -> None:
        super(install, self).run()
        os.environ["PYSDL3_DISABLE_DOCS"] = "0"
        sdl3 = __import__("sdl3")

        if not (len(sdl3.functions) > 0):
            print("something went wrong.", flush = True)

        else:
            print(f"loaded {len(sdl3.functions)} functions.", flush = True)

def main(argv):
    data = {
        "name": "PySDL3",
        "packages": ["sdl3", "sdl3.bin"],
        "version": "0.3.0a0",
        "description": "A pure Python wrapper for SDL3.",
        "long_description": open("README.md", "r", encoding = "utf-8").read(),
        "long_description_content_type": "text/markdown",
        "url": "https://github.com/Aermoss/PySDL3",
        "author": "Yusuf Rençber",
        "author_email": "aermoss.0@gmail.com",
        "license": "MIT",
        "include_package_data": True,
        "install_requires": [],
        "python_requires": ">=3.9",
        "cmdclass": {"install": CustomInstall}
    }

    setuptools.setup(**data)

if __name__ == "__main__":
    sys.exit(main(sys.argv))