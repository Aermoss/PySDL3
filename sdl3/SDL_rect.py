from .__init__ import ctypes, \
    SDL_FUNC, SDL_DEREFERENCE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_stdinc import SDL_FLT_EPSILON

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]
    
class SDL_FPoint(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float)
    ]

class SDL_Rect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int)
    ]

class SDL_FRect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("w", ctypes.c_float),
        ("h", ctypes.c_float)
    ]

class LP_SDL_Point(ctypes.POINTER(SDL_Point)):
    ...

class LP_SDL_FPoint(ctypes.POINTER(SDL_FPoint)):
    ...

class LP_SDL_Rect(ctypes.POINTER(SDL_Rect)):
    ...

class LP_SDL_FRect(ctypes.POINTER(SDL_FRect)):
    ...

def SDL_RectToFRect(rect: LP_SDL_Rect, frect: LP_SDL_FRect) -> None:
    rect, frect = SDL_DEREFERENCE(rect), SDL_DEREFERENCE(frect)
    frect.x, frect.y, frect.w, frect.h = \
        float(rect.x), float(rect.y), float(rect.w), float(rect.h)
    
def SDL_PointInRect(p: LP_SDL_Point, r: LP_SDL_Rect) -> bool:
    p, r = SDL_DEREFERENCE(p), SDL_DEREFERENCE(r)
    return p.x >= r.x and p.x < r.x + r.w and p.y >= r.y and p.y < r.y + r.h

def SDL_RectEmpty(r: LP_SDL_Rect) -> bool:
    r = SDL_DEREFERENCE(r)
    return r.w <= 0 or r.h <= 0

def SDL_RectEquals(a: LP_SDL_Rect, b: LP_SDL_Rect) -> bool:
    a, b = SDL_DEREFERENCE(a), SDL_DEREFERENCE(b)
    return a.x == b.x and a.y == b.y and a.w == b.w and a.h == b.h

SDL_FUNC("SDL_HasRectIntersection", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectIntersection", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectUnion", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectEnclosingPoints", ctypes.c_bool, ctypes.POINTER(SDL_Point), ctypes.c_int, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectAndLineIntersection", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def SDL_PointInRectFloat(p: LP_SDL_FPoint, r: LP_SDL_FRect) -> bool:
    p, r = SDL_DEREFERENCE(p), SDL_DEREFERENCE(r)
    return p.x >= r.x and p.x < r.x + r.w and p.y >= r.y and p.y < r.y + r.h

def SDL_RectEmptyFloat(r: LP_SDL_FRect) -> bool:
    r = SDL_DEREFERENCE(r)
    return r.w <= 0 or r.h <= 0

def SDL_RectsEqualEpsilon(a: LP_SDL_FRect, b: LP_SDL_FRect, epsilon: float) -> bool:
    a, b = SDL_DEREFERENCE(a), SDL_DEREFERENCE(b)
    return abs(a.x - b.x) < epsilon and abs(a.y - b.y) < epsilon and abs(a.w - b.w) < epsilon and abs(a.h - b.h) < epsilon

def SDL_RectsEqualFloat(a: LP_SDL_FRect, b: LP_SDL_FRect) -> bool:
    a, b = SDL_DEREFERENCE(a), SDL_DEREFERENCE(b)
    return SDL_RectsEqualEpsilon(a, b, SDL_FLT_EPSILON)

SDL_FUNC("SDL_HasRectIntersectionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectIntersectionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectUnionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectEnclosingPointsFloat", ctypes.c_bool, ctypes.POINTER(SDL_FPoint), ctypes.c_int, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectAndLineIntersectionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))