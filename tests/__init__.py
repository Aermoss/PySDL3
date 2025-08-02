"""
PySDL3 Test Suite

This package contains tests for PySDL3 functionality, including:
- Core functionality tests (TEST_*.py)
- Custom libraries test suite (TEST_custom_libraries.py)

For custom compiled SDL3 libraries, use the setup utility in the project root:
    python3 custom_libraries_setup.py /path/to/custom/libraries
    python3 tests/TEST_custom_libraries.py /path/to/custom/libraries
"""

import os, sys, collections.abc as abc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sdl3, ctypes, atexit, traceback

functions: dict[abc.Callable[..., None], list[str]] = {}

def TEST_RegisterFunction(systems: list[str]) -> abc.Callable[[abc.Callable[..., None]], None]:
    return lambda func: functions.update({func: systems})

from tests.TEST_init import *
from tests.TEST_locale import *
from tests.TEST_version import *
from tests.TEST_video import *
from tests.TEST_coverage_evaluation import *
from tests.TEST_module_analyzer import *
from tests.TEST_runner import *

@atexit.register
def TEST_RunAllTests() -> None:
    if not functions: return
    print("\33[32m", f"Initializing tests... (version: {sdl3.__version__}, system: {sdl3.SDL_SYSTEM}, arch: {sdl3.SDL_ARCH}).", "\33[0m", sep = "", flush = True)
    passed, failed = 0, 0

    for func, systems in functions.items():
        try:
            if sdl3.SDL_SYSTEM not in systems:
                print("\33[33m", f"Test '{func.__name__}' is not supported on {sdl3.SDL_SYSTEM}.", "\33[0m", sep = "", flush = True)

            else:
                sdl3.SDL_ClearError(); func()
                print("\33[32m", f"Test '{func.__name__}' passed.", "\33[0m", sep = "", flush = True)
                passed += 1

        except AssertionError as exc:
            print("\33[31m", f"Test '{func.__name__}' failed: {str(exc).capitalize()}", "\33[0m", sep = "", flush = True)
            failed += 1
        
        except Exception as exc:
            print("\33[31m", f"Test '{func.__name__}' failed: {str(exc).capitalize()}.\n\n{traceback.format_exc()}", "\33[0m", sep = "", flush = True)
            os._exit(-1)

    print("\33[31m" if failed else "\33[32m", f"{'Failed' if failed else 'Passed'}! {passed} test(s) passed, {failed} test(s) failed.", "\33[0m", sep = "", flush = True)
    if failed: os._exit(-1)