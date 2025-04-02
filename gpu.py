import sys, os, subprocess

try: __import__("embed").main(sys.argv)
except ModuleNotFoundError: ...

import sdl3, shader, ctypes, time, colorsys

def compileShader(name, size = ctypes.c_size_t()):
    subprocess.run(["glslc", f"{name}.glsl", "-o", f"{name}.spv"])
    data = sdl3.SDL_LoadFile(f"{name}.spv".encode(), ctypes.byref(size))
    return size.value, ctypes.cast(data, sdl3.SDL_POINTER[ctypes.c_uint8])

class Vertex(ctypes.Structure):
    _fields_ = [
        ("position", ctypes.c_float * 3),
        ("color", ctypes.c_float * 3)
    ]

class UniformData(ctypes.Structure):
    _fields_ = [
        ("color0", ctypes.c_float * 4),
        ("color1", ctypes.c_float * 4),
        ("color2", ctypes.c_float * 4)
    ]

@sdl3.SDL_main_func
def main(argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> ctypes.c_int:
    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS | sdl3.SDL_INIT_AUDIO):
        print(f"Failed to initialize library: {sdl3.SDL_GetError().decode()}.")
        return -1
    
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1600, 900, sdl3.SDL_WINDOW_RESIZABLE)
    event, running = sdl3.SDL_Event(), True

    gpuDrivers = [sdl3.SDL_GetGPUDriver(i).decode() for i in range(sdl3.SDL_GetNumGPUDrivers())]
    tryGetDriver, tryUseVulkan = lambda order, drivers: next((i for i in order if i in drivers), None), True
    gpuDriver = tryGetDriver(["vulkan"] if tryUseVulkan else [], gpuDrivers)
    print(f"Available GPU drivers: {', '.join(gpuDrivers)} (current: {gpuDriver}).")

    if not (device := sdl3.SDL_CreateGPUDevice(sdl3.SDL_GPU_SHADERFORMAT_SPIRV, True, gpuDriver.encode())):
        print(f"Failed to create GPU device: {sdl3.SDL_GetError().decode()}.")
        return -1

    if not sdl3.SDL_ClaimWindowForGPUDevice(device, window):
        print(f"Failed to claim window for GPU device: {sdl3.SDL_GetError().decode()}")
        return -1

    vertexShader = sdl3.SDL_CreateGPUShader(device, sdl3.SDL_GPUShaderCreateInfo(*shader.vertexData, entrypoint = "main".encode(), format = sdl3.SDL_GPU_SHADERFORMAT_SPIRV, stage = sdl3.SDL_GPU_SHADERSTAGE_VERTEX, num_uniform_buffers = 1))
    fragmentShader = sdl3.SDL_CreateGPUShader(device, sdl3.SDL_GPUShaderCreateInfo(*shader.fragmentData, entrypoint = "main".encode(), format = sdl3.SDL_GPU_SHADERFORMAT_SPIRV, stage = sdl3.SDL_GPU_SHADERSTAGE_FRAGMENT))

    pipeline = sdl3.SDL_CreateGPUGraphicsPipeline(device, sdl3.SDL_GPUGraphicsPipelineCreateInfo(vertexShader, fragmentShader, primitive_type = sdl3.SDL_GPU_PRIMITIVETYPE_TRIANGLELIST,
        target_info = sdl3.SDL_GPUGraphicsPipelineTargetInfo(*sdl3.SDL_ARRAY(sdl3.SDL_GPUColorTargetDescription(sdl3.SDL_GetGPUSwapchainTextureFormat(device, window)))),
        vertex_input_state = sdl3.SDL_GPUVertexInputState(*sdl3.SDL_ARRAY(sdl3.SDL_GPUVertexBufferDescription(0, ctypes.sizeof(Vertex), sdl3.SDL_GPU_VERTEXINPUTRATE_VERTEX, 0)),
            *sdl3.SDL_ARRAY(sdl3.SDL_GPUVertexAttribute(0, 0, sdl3.SDL_GPU_VERTEXELEMENTFORMAT_FLOAT3, 0)))
    ))
    
    sdl3.SDL_ReleaseGPUShader(device, fragmentShader)
    sdl3.SDL_ReleaseGPUShader(device, vertexShader)
    
    if not pipeline:
        print(f"Failed to create GPU pipeline: {sdl3.SDL_GetError().decode()}.")
        return -1
    
    vertexBuffer = sdl3.SDL_CreateGPUBuffer(device, sdl3.SDL_GPUBufferCreateInfo(sdl3.SDL_GPU_BUFFERUSAGE_VERTEX, ctypes.sizeof(Vertex) * 3))
    transferBuffer = sdl3.SDL_CreateGPUTransferBuffer(device, sdl3.SDL_GPUTransferBufferCreateInfo(sdl3.SDL_GPU_TRANSFERBUFFERUSAGE_UPLOAD, ctypes.sizeof(Vertex) * 3))

    transferData = ctypes.cast(sdl3.SDL_MapGPUTransferBuffer(device, transferBuffer, False), sdl3.SDL_POINTER[Vertex])
    transferData[0] = Vertex(sdl3.SDL_ARRAY(-0.5, -0.5, 0.0, type = ctypes.c_float)[0])
    transferData[1] = Vertex(sdl3.SDL_ARRAY( 0.5, -0.5, 0.0, type = ctypes.c_float)[0])
    transferData[2] = Vertex(sdl3.SDL_ARRAY( 0.0,  0.5, 0.0, type = ctypes.c_float)[0])
    sdl3.SDL_UnmapGPUTransferBuffer(device, transferBuffer)

    commandBuffer = sdl3.SDL_AcquireGPUCommandBuffer(device)
    copyPass = sdl3.SDL_BeginGPUCopyPass(commandBuffer)
    sdl3.SDL_UploadToGPUBuffer(copyPass, sdl3.SDL_GPUTransferBufferLocation(transferBuffer, 0), sdl3.SDL_GPUBufferRegion(vertexBuffer, 0, ctypes.sizeof(Vertex) * 3), False)
    sdl3.SDL_EndGPUCopyPass(copyPass)

    sdl3.SDL_SubmitGPUCommandBuffer(commandBuffer)
    sdl3.SDL_ReleaseGPUTransferBuffer(device, transferBuffer)
    uniformData, lastTime, hue = UniformData(), time.time(), 0.0

    while running:
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            match event.type:
                case sdl3.SDL_EVENT_QUIT:
                    running = False

                case sdl3.SDL_EVENT_KEY_DOWN:
                    if event.key.key == sdl3.SDLK_ESCAPE:
                        running = False

        commandBuffer = sdl3.SDL_AcquireGPUCommandBuffer(device)

        if not commandBuffer:
            print(f"Failed to acquire GPU command buffer: {sdl3.SDL_GetError().decode()}.")
            return -1

        swapChainTexture = sdl3.LP_SDL_GPUTexture()
        sdl3.SDL_WaitAndAcquireGPUSwapchainTexture(commandBuffer, window, ctypes.byref(swapChainTexture), None, None)

        if not swapChainTexture:
            print(f"Failed to acquire GPU swapchain texture: {sdl3.SDL_GetError().decode()}.")
            return -1
        
        lastTime, deltaTime = \
            time.time(), time.time() - lastTime

        colorTargetInfo = sdl3.SDL_GPUColorTargetInfo(swapChainTexture, load_op = sdl3.SDL_GPU_LOADOP_CLEAR,
            clear_color = sdl3.SDL_FColor(*colorsys.hsv_to_rgb(hue := (hue + 0.25 * deltaTime) % 1, 1.0, 0.0), 1.0))
        
        uniformData.color0 = sdl3.SDL_ARRAY(*colorsys.hsv_to_rgb(hue + 0.48, 1.0, 1.0), 1.0, type = ctypes.c_float)[0]
        uniformData.color1 = sdl3.SDL_ARRAY(*colorsys.hsv_to_rgb(hue + 0.32, 1.0, 1.0), 1.0, type = ctypes.c_float)[0]
        uniformData.color2 = sdl3.SDL_ARRAY(*colorsys.hsv_to_rgb(hue + 0.64, 1.0, 1.0), 1.0, type = ctypes.c_float)[0]

        renderPass = sdl3.SDL_BeginGPURenderPass(commandBuffer, ctypes.byref(colorTargetInfo), 1, None)
        sdl3.SDL_BindGPUGraphicsPipeline(renderPass, pipeline)
        sdl3.SDL_BindGPUVertexBuffers(renderPass, 0, sdl3.SDL_GPUBufferBinding(vertexBuffer, 0), 1)
        sdl3.SDL_PushGPUVertexUniformData(commandBuffer, 0, ctypes.byref(uniformData), ctypes.sizeof(uniformData))
        sdl3.SDL_DrawGPUPrimitives(renderPass, 3, 1, 0, 0)
        sdl3.SDL_EndGPURenderPass(renderPass)

        sdl3.SDL_SubmitGPUCommandBuffer(commandBuffer)

    sdl3.SDL_ReleaseGPUBuffer(device, vertexBuffer)
    sdl3.SDL_ReleaseGPUGraphicsPipeline(device, pipeline)
    sdl3.SDL_DestroyGPUDevice(device)

    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0