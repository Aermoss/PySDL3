from .__init__ import ctypes, typing, SDL_TYPE, SDL_ENUM

from .SDL_touch import SDL_TouchID
from .SDL_mouse import SDL_MouseID

SDL_PenID: typing.TypeAlias = SDL_TYPE["SDL_PenID", ctypes.c_uint32]

SDL_PEN_MOUSEID, SDL_PEN_TOUCHID = SDL_MouseID(-2), SDL_TouchID(-2)

SDL_PenInputFlags: typing.TypeAlias = SDL_TYPE["SDL_PenInputFlags", ctypes.c_uint32]

SDL_PEN_INPUT_DOWN = 1 << 0
SDL_PEN_INPUT_BUTTON_1 = 1 << 1
SDL_PEN_INPUT_BUTTON_2 = 1 << 2
SDL_PEN_INPUT_BUTTON_3 = 1 << 3
SDL_PEN_INPUT_BUTTON_4 = 1 << 4
SDL_PEN_INPUT_BUTTON_5 = 1 << 5
SDL_PEN_INPUT_ERASER_TIP = 1 << 30

SDL_PenAxis: typing.TypeAlias = SDL_TYPE["SDL_PenAxis", SDL_ENUM]

SDL_PEN_AXIS_PRESSURE, SDL_PEN_AXIS_XTILT, SDL_PEN_AXIS_YTILT, SDL_PEN_AXIS_DISTANCE, SDL_PEN_AXIS_ROTATION, \
    SDL_PEN_AXIS_SLIDER, SDL_PEN_AXIS_TANGENTIAL_PRESSURE, SDL_PEN_AXIS_COUNT = range(8)