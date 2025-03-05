import os, sys, typing, collections.abc as abc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

os.environ["SDL_DOC_GENERATOR"] = "0"

import sdl3, ctypes, atexit

functions = {}

def TEST_RegisterFunction(systems: list[str]) -> abc.Callable[[abc.Callable[..., typing.Any]], None]:
    return lambda func: functions.update({func: systems})

class TEST_PassFunction(Exception):
    ...

from tests.TEST_init import *
from tests.TEST_video import *

@atexit.register
def TEST_RunAllTests() -> None:
    if not functions: return
    print("\33[32m", f"Initializing tests... (Version: {sdl3.__version__}, System: {sdl3.SDL_SYSTEM}, Arch: {sdl3.SDL_ARCH})", "\33[0m", sep = "", flush = True)
    passed, failed = 0, 0

    for func, systems in functions.items():
        try:
            sdl3.SDL_ClearError()
            if sdl3.SDL_SYSTEM in systems: func()
            else: raise TEST_PassFunction()
            print("\33[32m", f"Test '{func.__name__}' passed.", "\33[0m", sep = "", flush = True)
            passed += 1

        except TEST_PassFunction as error:
            print("\33[33m", f"Test '{func.__name__}' is not supported on {sdl3.SDL_SYSTEM}.", "\33[0m", sep = "", flush = True)

        except AssertionError as error:
            print("\33[31m", f"Test '{func.__name__}' failed: {error}", "\33[0m", sep = "", flush = True)
            failed += 1

    print("\33[31m" if failed else "\33[32m", f"{'Failed' if failed else 'Passed'}! {passed} test(s) passed, {failed} test(s) failed.", "\33[0m", sep = "", flush = True)
    if failed: os._exit(-1)