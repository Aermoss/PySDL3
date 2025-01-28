import os, sys, atexit

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sdl3

functions = []

def TEST_RegisterFunction(func):
    functions.append(func)

from tests.TEST_init import *

@atexit.register
def TEST_RunAllTests():
    if not functions: return
    successful, failed = 0, 0

    for func in functions:
        try:
            func()
            print("\33[32m", f"Test '{func.__name__}' passed.", "\33[0m", sep = "", flush = True)
            successful += 1

        except AssertionError as error:
            print("\33[31m", f"Test '{func.__name__}' failed: {error}", "\33[0m", sep = "", flush = True)
            failed += 1

    print("\33[35m", f"{successful} test(s) passed, {failed} test(s) failed.", "\33[0m", sep = "", flush = True)
    if failed: os._exit(-1)