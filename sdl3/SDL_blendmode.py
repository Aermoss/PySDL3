from .__init__ import ctypes, typing, abc, \
    SDL_ENUM, SDL_FUNC, SDL_TYPE, SDL_BINARY

SDL_BlendMode: typing.TypeAlias = SDL_TYPE["SDL_BlendMode", ctypes.c_uint32]

SDL_BLENDMODE_NONE: int = 0x00000000
SDL_BLENDMODE_BLEND: int = 0x00000001
SDL_BLENDMODE_BLEND_PREMULTIPLIED: int = 0x00000010
SDL_BLENDMODE_ADD: int = 0x00000002
SDL_BLENDMODE_ADD_PREMULTIPLIED: int = 0x00000020
SDL_BLENDMODE_MOD: int = 0x00000004
SDL_BLENDMODE_MUL: int = 0x00000008
SDL_BLENDMODE_INVALID: int = 0x7FFFFFFF

SDL_BlendOperation: typing.TypeAlias = SDL_TYPE["SDL_BlendOperation", SDL_ENUM]

SDL_BLENDOPERATION_ADD, SDL_BLENDOPERATION_SUBTRACT, SDL_BLENDOPERATION_REV_SUBTRACT, \
    SDL_BLENDOPERATION_MINIMUM, SDL_BLENDOPERATION_MAXIMUM = range(1, 6)

SDL_BlendFactor: typing.TypeAlias = SDL_TYPE["SDL_BlendFactor", SDL_ENUM]

SDL_BLENDFACTOR_ZERO, SDL_BLENDFACTOR_ONE, SDL_BLENDFACTOR_SRC_COLOR, SDL_BLENDFACTOR_ONE_MINUS_SRC_COLOR, \
    SDL_BLENDFACTOR_SRC_ALPHA, SDL_BLENDFACTOR_ONE_MINUS_SRC_ALPHA, SDL_BLENDFACTOR_DST_COLOR, SDL_BLENDFACTOR_ONE_MINUS_DST_COLOR, \
        SDL_BLENDFACTOR_DST_ALPHA, SDL_BLENDFACTOR_ONE_MINUS_DST_ALPHA = range(1, 11)

SDL_ComposeCustomBlendMode: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ComposeCustomBlendMode", SDL_BlendMode, [SDL_BlendFactor, SDL_BlendFactor, SDL_BlendOperation, SDL_BlendFactor, SDL_BlendFactor, SDL_BlendOperation], SDL_BINARY]