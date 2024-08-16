from .__init__ import ctypes, SDL_FUNC

from .SDL_video import SDL_Window
from .SDL_stdinc import SDL_FunctionPointer

class VkInstance(ctypes.Structure):
    ...

class VkPhysicalDevice(ctypes.Structure):
    ...

class VkAllocationCallbacks(ctypes.Structure):
    ...
    
VkSurfaceKHR = ctypes.c_uint64

SDL_FUNC("SDL_Vulkan_LoadLibrary", ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_Vulkan_GetVkGetInstanceProcAddr", SDL_FunctionPointer)
SDL_FUNC("SDL_Vulkan_UnloadLibrary", None)
SDL_FUNC("SDL_Vulkan_GetInstanceExtensions", ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint32))

SDL_FUNC("SDL_Vulkan_CreateSurface", ctypes.c_int, ctypes.POINTER(SDL_Window), VkInstance, ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(VkSurfaceKHR))
SDL_FUNC("SDL_Vulkan_DestroySurface", None, VkInstance, VkSurfaceKHR, ctypes.POINTER(VkAllocationCallbacks))
SDL_FUNC("SDL_Vulkan_GetPresentationSupport", ctypes.c_bool, VkInstance, VkPhysicalDevice, ctypes.c_uint32)