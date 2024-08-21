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
        "version": "0.4.0a3",
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