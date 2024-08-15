from .__init__ import ctypes, SDL_FUNC

from .SDL_stdinc import SDL_FLT_EPSILON

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

def SDL_RectToFRect(rect: SDL_Rect, frect: SDL_FRect) -> None:
    frect.x, frect.y, frect.w, frect.h = \
        float(rect.x), float(rect.y), float(rect.w), float(rect.h)
    
def SDL_PointInRect(p: SDL_Point, r: SDL_Rect) -> bool:
    return p.x >= r.x and p.x < r.x + r.w and p.y >= r.y and p.y < r.y + r.h

def SDL_RectEmpty(r: SDL_Rect) -> bool:
    return r.w <= 0 or r.h <= 0

def SDL_RectEquals(a: SDL_Rect, b: SDL_Rect) -> bool:
    return a.x == b.x and a.y == b.y and a.w == b.w and a.h == b.h

SDL_FUNC("SDL_HasRectIntersection", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectIntersection", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectUnion", ctypes.c_int, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectEnclosingPoints", ctypes.c_bool, ctypes.POINTER(SDL_Point), ctypes.c_int, ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRectAndLineIntersection", ctypes.c_bool, ctypes.POINTER(SDL_Rect), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def SDL_PointInRectFloat(p: SDL_FPoint, r: SDL_FRect) -> bool:
    return p.x >= r.x and p.x < r.x + r.w and p.y >= r.y and p.y < r.y + r.h

def SDL_RectEmptyFloat(r: SDL_FRect) -> bool:
    return r.w <= 0 or r.h <= 0

def SDL_RectsEqualEpsilon(a: SDL_FRect, b: SDL_FRect, epsilon: float) -> bool:
    return abs(a.x - b.x) < epsilon and abs(a.y - b.y) < epsilon and abs(a.w - b.w) < epsilon and abs(a.h - b.h) < epsilon

def SDL_RectsEqualFloat(a: SDL_FRect, b: SDL_FRect) -> bool:
    return SDL_RectsEqualEpsilon(a, b, SDL_FLT_EPSILON)

SDL_FUNC("SDL_HasRectIntersectionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectIntersectionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectUnionFloat", ctypes.c_int, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectEnclosingPointsFloat", ctypes.c_bool, ctypes.POINTER(SDL_FPoint), ctypes.c_int, ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_GetRectAndLineIntersectionFloat", ctypes.c_bool, ctypes.POINTER(SDL_FRect), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))