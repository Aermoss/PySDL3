from .__init__ import sys, os, ctypes, atexit, SDL_GET_DLL, SDL_DLL

from .SDL_main import SDL_main_func

class LP_c_char_p(ctypes.POINTER(ctypes.c_char_p)): ...

if not int(os.environ.get("SDL_MAIN_HANDLED", "0")) > 0 and not int(os.environ.get("SDL_MAIN_NOIMPL", "0")) > 0:
    import __main__

    if int(os.environ.get("SDL_MAIN_USE_CALLBACKS", "0")) > 0:
        @SDL_main_func
        def SDL_main(argc: ctypes.c_int, argv: LP_c_char_p) -> ctypes.c_int:
            return SDL_GET_DLL(SDL_DLL).SDL_EnterAppMainCallbacks(argc, argv, *[getattr(__main__, i, None) for i in ["SDL_AppInit", "SDL_AppIterate", "SDL_AppEvent", "SDL_AppQuit"]])
        
        os.environ["SDL_MAIN_CALLBACK_STANDARD"] = "1"
        setattr(__main__, "SDL_main", SDL_main)

    if (not int(os.environ.get("SDL_MAIN_USE_CALLBACKS", "0")) > 0 or int(os.environ.get("SDL_MAIN_CALLBACK_STANDARD", "0")) > 0) and not int(os.environ.get("SDL_MAIN_EXPORTED", "0")) > 0:
        @atexit.register
        def SDL_ATEXIT_HANDLER() -> ...:
            if main := (getattr(__main__, "SDL_main", None) or getattr(__main__, "main", None)):
                return SDL_GET_DLL(SDL_DLL).SDL_RunApp(len(sys.argv), (ctypes.c_char_p * len(sys.argv))(*[i.encode() for i in sys.argv]), main, None)