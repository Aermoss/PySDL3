#!/usr/bin/env python3
"""
PySDL3 Coverage Evaluation Test Script

This script comprehensively tests the coverage and functionality of PySDL3
across all supported SDL3 libraries:
- SDL3 (core)
- SDL3_image
- SDL3_mixer  
- SDL3_ttf
- SDL3_rtf
- SDL3_net
- SDL3_shadercross
"""

import sys
import os
import traceback
import time
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum

# Handle both direct execution and test framework import
try:
    from .__init__ import sdl3, TEST_RegisterFunction
except ImportError:
    # When run directly, add parent directory to path
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    import sdl3
    
    # Define a dummy TEST_RegisterFunction for standalone execution
    def TEST_RegisterFunction(systems):
        def decorator(func):
            return func
        return decorator

class TestResult(Enum):
    PASS = "✅"
    FAIL = "❌"
    SKIP = "⏭️"
    WARN = "⚠️"

@dataclass
class TestCase:
    name: str
    description: str
    result: TestResult
    details: str = ""
    error: Optional[str] = None

class PySDL3CoverageTest:
    def __init__(self):
        self.results: List[TestCase] = []
        self.stats = {
            TestResult.PASS: 0,
            TestResult.FAIL: 0,
            TestResult.SKIP: 0,
            TestResult.WARN: 0
        }
        
    def add_result(self, test_case: TestCase):
        self.results.append(test_case)
        self.stats[test_case.result] += 1
        
    def test_function_exists(self, module_name: str, func_name: str) -> bool:
        """Test if a function exists in the given module."""
        try:
            module = getattr(sdl3, module_name, None)
            if module is None:
                return hasattr(sdl3, func_name)
            return hasattr(sdl3, func_name)
        except:
            return False
    
    def test_constant_exists(self, const_name: str) -> bool:
        """Test if a constant exists in SDL3."""
        return hasattr(sdl3, const_name)
    
    def test_structure_exists(self, struct_name: str) -> bool:
        """Test if a structure exists in SDL3."""
        return hasattr(sdl3, struct_name)

    def test_sdl3_core(self):
        """Test SDL3 core functionality coverage."""
        print("🔍 Testing SDL3 Core Library...")
        
        # Test basic initialization
        try:
            # Test version functions
            version_funcs = ['SDL_GetVersion', 'SDL_GetRevision']
            for func in version_funcs:
                if self.test_function_exists('', func):
                    self.add_result(TestCase(
                        f"SDL3 Core - {func}",
                        f"Function {func} exists",
                        TestResult.PASS
                    ))
                else:
                    self.add_result(TestCase(
                        f"SDL3 Core - {func}",
                        f"Function {func} missing",
                        TestResult.FAIL
                    ))
            
            # Test initialization functions
            init_funcs = ['SDL_Init', 'SDL_Quit', 'SDL_InitSubSystem', 'SDL_QuitSubSystem']
            for func in init_funcs:
                if self.test_function_exists('', func):
                    self.add_result(TestCase(
                        f"SDL3 Core - {func}",
                        f"Function {func} exists",
                        TestResult.PASS
                    ))
                else:
                    self.add_result(TestCase(
                        f"SDL3 Core - {func}",
                        f"Function {func} missing",
                        TestResult.FAIL
                    ))
            
            # Test subsystem constants
            subsystem_constants = [
                'SDL_INIT_TIMER', 'SDL_INIT_AUDIO', 'SDL_INIT_VIDEO',
                'SDL_INIT_JOYSTICK', 'SDL_INIT_HAPTIC', 'SDL_INIT_GAMEPAD',
                'SDL_INIT_EVENTS', 'SDL_INIT_SENSOR', 'SDL_INIT_CAMERA'
            ]
            
            for const in subsystem_constants:
                if self.test_constant_exists(const):
                    self.add_result(TestCase(
                        f"SDL3 Core - {const}",
                        f"Constant {const} exists",
                        TestResult.PASS
                    ))
                else:
                    self.add_result(TestCase(
                        f"SDL3 Core - {const}",
                        f"Constant {const} missing",
                        TestResult.FAIL
                    ))
            
            # Test key structures
            core_structures = [
                'SDL_Window', 'SDL_Surface', 'SDL_Texture', 'SDL_Renderer',
                'SDL_Event', 'SDL_Rect', 'SDL_Point', 'SDL_Color'
            ]
            
            for struct in core_structures:
                if self.test_structure_exists(struct):
                    self.add_result(TestCase(
                        f"SDL3 Core - {struct}",
                        f"Structure {struct} exists",
                        TestResult.PASS
                    ))
                else:
                    self.add_result(TestCase(
                        f"SDL3 Core - {struct}",
                        f"Structure {struct} missing",
                        TestResult.FAIL
                    ))
                    
        except Exception as e:
            self.add_result(TestCase(
                "SDL3 Core - General Test",
                "Error during core testing",
                TestResult.FAIL,
                error=str(e)
            ))

    def test_sdl3_video(self):
        """Test SDL3 video subsystem coverage."""
        print("🎮 Testing SDL3 Video Subsystem...")
        
        video_functions = [
            'SDL_CreateWindow', 'SDL_DestroyWindow', 'SDL_ShowWindow',
            'SDL_HideWindow', 'SDL_GetWindowSize', 'SDL_SetWindowSize',
            'SDL_GetWindowPosition', 'SDL_SetWindowPosition',
            'SDL_CreateRenderer', 'SDL_DestroyRenderer',
            'SDL_RenderClear', 'SDL_RenderPresent'
        ]
        
        for func in video_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3 Video - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3 Video - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test window flags
        window_flags = [
            'SDL_WINDOW_FULLSCREEN', 'SDL_WINDOW_OPENGL', 'SDL_WINDOW_HIDDEN',
            'SDL_WINDOW_BORDERLESS', 'SDL_WINDOW_RESIZABLE', 'SDL_WINDOW_MINIMIZED',
            'SDL_WINDOW_MAXIMIZED'
        ]
        
        for flag in window_flags:
            if self.test_constant_exists(flag):
                self.add_result(TestCase(
                    f"SDL3 Video - {flag}",
                    f"Window flag {flag} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3 Video - {flag}",
                    f"Window flag {flag} missing",
                    TestResult.FAIL
                ))

    def test_sdl3_audio(self):
        """Test SDL3 audio subsystem coverage."""
        print("🔊 Testing SDL3 Audio Subsystem...")
        
        audio_functions = [
            'SDL_OpenAudioDevice', 'SDL_CloseAudioDevice', 'SDL_PauseAudioDevice',
            'SDL_GetAudioDeviceName', 'SDL_GetNumAudioDevices',
            'SDL_LoadWAV', 'SDL_FreeWAV'
        ]
        
        for func in audio_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3 Audio - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3 Audio - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test audio formats
        audio_formats = [
            'SDL_AUDIO_U8', 'SDL_AUDIO_S8', 'SDL_AUDIO_S16', 'SDL_AUDIO_S32',
            'SDL_AUDIO_F32'
        ]
        
        for fmt in audio_formats:
            if self.test_constant_exists(fmt):
                self.add_result(TestCase(
                    f"SDL3 Audio - {fmt}",
                    f"Audio format {fmt} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3 Audio - {fmt}",
                    f"Audio format {fmt} missing",
                    TestResult.FAIL
                ))

    def test_sdl3_image(self):
        """Test SDL3_image library coverage."""
        print("🖼️ Testing SDL3_image Library...")
        
        # Test core image functions
        image_functions = [
            'IMG_Init', 'IMG_Quit', 'IMG_Load', 'IMG_Load_IO',
            'IMG_LoadTexture', 'IMG_LoadTexture_IO',
            'IMG_SavePNG', 'IMG_SaveJPG'
        ]
        
        for func in image_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_image - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_image - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test format detection functions
        format_functions = [
            'IMG_isAVIF', 'IMG_isBMP', 'IMG_isGIF', 'IMG_isJPG',
            'IMG_isPNG', 'IMG_isSVG', 'IMG_isWEBP', 'IMG_isTIF'
        ]
        
        for func in format_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_image - {func}",
                    f"Format detection {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_image - {func}",
                    f"Format detection {func} missing",
                    TestResult.FAIL
                ))
        
        # Test animation support
        animation_functions = [
            'IMG_LoadAnimation', 'IMG_LoadAnimation_IO',
            'IMG_FreeAnimation', 'IMG_LoadGIFAnimation_IO'
        ]
        
        for func in animation_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_image - {func}",
                    f"Animation function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_image - {func}",
                    f"Animation function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test IMG_Animation structure
        if self.test_structure_exists('IMG_Animation'):
            self.add_result(TestCase(
                "SDL3_image - IMG_Animation",
                "IMG_Animation structure exists",
                TestResult.PASS
            ))
        else:
            self.add_result(TestCase(
                "SDL3_image - IMG_Animation",
                "IMG_Animation structure missing",
                TestResult.FAIL
            ))

    def test_sdl3_mixer(self):
        """Test SDL3_mixer library coverage."""
        print("🎵 Testing SDL3_mixer Library...")
        
        # Test core mixer functions
        mixer_functions = [
            'Mix_Init', 'Mix_Quit', 'Mix_OpenAudio', 'Mix_CloseAudio',
            'Mix_LoadWAV', 'Mix_LoadMUS', 'Mix_FreeChunk', 'Mix_FreeMusic',
            'Mix_PlayChannel', 'Mix_PlayMusic', 'Mix_HaltChannel', 'Mix_HaltMusic'
        ]
        
        for func in mixer_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_mixer - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_mixer - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test format support constants
        mixer_formats = [
            'MIX_INIT_FLAC', 'MIX_INIT_MOD', 'MIX_INIT_MP3',
            'MIX_INIT_OGG', 'MIX_INIT_MID', 'MIX_INIT_OPUS'
        ]
        
        for fmt in mixer_formats:
            if self.test_constant_exists(fmt):
                self.add_result(TestCase(
                    f"SDL3_mixer - {fmt}",
                    f"Format constant {fmt} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_mixer - {fmt}",
                    f"Format constant {fmt} missing",
                    TestResult.FAIL
                ))
        
        # Test structures
        mixer_structures = ['Mix_Chunk', 'Mix_Music']
        for struct in mixer_structures:
            if self.test_structure_exists(struct):
                self.add_result(TestCase(
                    f"SDL3_mixer - {struct}",
                    f"Structure {struct} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_mixer - {struct}",
                    f"Structure {struct} missing",
                    TestResult.FAIL
                ))

    def test_sdl3_ttf(self):
        """Test SDL3_ttf library coverage."""
        print("🔤 Testing SDL3_ttf Library...")
        
        # Test core TTF functions
        ttf_functions = [
            'TTF_Init', 'TTF_Quit', 'TTF_OpenFont', 'TTF_OpenFontIO',
            'TTF_CloseFont', 'TTF_RenderText_Solid', 'TTF_RenderText_Shaded',
            'TTF_RenderText_Blended', 'TTF_GetFontHeight', 'TTF_GetFontAscent'
        ]
        
        for func in ttf_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_ttf - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_ttf - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test font style constants
        ttf_styles = [
            'TTF_STYLE_NORMAL', 'TTF_STYLE_BOLD', 'TTF_STYLE_ITALIC',
            'TTF_STYLE_UNDERLINE', 'TTF_STYLE_STRIKETHROUGH'
        ]
        
        for style in ttf_styles:
            if self.test_constant_exists(style):
                self.add_result(TestCase(
                    f"SDL3_ttf - {style}",
                    f"Style constant {style} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_ttf - {style}",
                    f"Style constant {style} missing",
                    TestResult.FAIL
                ))
        
        # Test TTF_Font structure
        if self.test_structure_exists('TTF_Font'):
            self.add_result(TestCase(
                "SDL3_ttf - TTF_Font",
                "TTF_Font structure exists",
                TestResult.PASS
            ))
        else:
            self.add_result(TestCase(
                "SDL3_ttf - TTF_Font",
                "TTF_Font structure missing",
                TestResult.FAIL
            ))

    def test_sdl3_net(self):
        """Test SDL3_net library coverage."""
        print("🌐 Testing SDL3_net Library...")
        
        # Test core NET functions
        net_functions = [
            'NET_Init', 'NET_Quit', 'NET_ResolveHostname', 'NET_GetAddressString',
            'NET_CreateClient', 'NET_CreateServer', 'NET_AcceptClient',
            'NET_WriteToStreamSocket', 'NET_ReadFromStreamSocket',
            'NET_CreateDatagramSocket', 'NET_SendDatagram', 'NET_ReceiveDatagram'
        ]
        
        for func in net_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_net - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_net - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test NET structures
        net_structures = [
            'NET_Address', 'NET_StreamSocket', 'NET_Server',
            'NET_DatagramSocket', 'NET_Datagram'
        ]
        
        for struct in net_structures:
            if self.test_structure_exists(struct):
                self.add_result(TestCase(
                    f"SDL3_net - {struct}",
                    f"Structure {struct} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_net - {struct}",
                    f"Structure {struct} missing",
                    TestResult.FAIL
                ))

    def test_sdl3_rtf(self):
        """Test SDL3_rtf library coverage."""
        print("📄 Testing SDL3_rtf Library...")
        
        # Test core RTF functions
        rtf_functions = [
            'RTF_CreateContext', 'RTF_Load', 'RTF_Load_IO',
            'RTF_GetTitle', 'RTF_GetAuthor', 'RTF_GetSubject',
            'RTF_GetHeight', 'RTF_Render', 'RTF_FreeContext'
        ]
        
        for func in rtf_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_rtf - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_rtf - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test RTF structures and enums
        rtf_types = ['RTF_Context', 'RTF_FontEngine', 'RTF_FontFamily', 'RTF_FontStyle']
        
        for type_name in rtf_types:
            if self.test_structure_exists(type_name):
                self.add_result(TestCase(
                    f"SDL3_rtf - {type_name}",
                    f"Type {type_name} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_rtf - {type_name}",
                    f"Type {type_name} missing",
                    TestResult.FAIL
                ))

    def test_sdl3_shadercross(self):
        """Test SDL3_shadercross library coverage."""
        print("🔧 Testing SDL3_shadercross Library...")
        
        # Test core ShaderCross functions
        shadercross_functions = [
            'SDL_ShaderCross_Init', 'SDL_ShaderCross_Quit',
            'SDL_ShaderCross_GetSPIRVShaderFormats',
            'SDL_ShaderCross_TranspileMSLFromSPIRV',
            'SDL_ShaderCross_TranspileHLSLFromSPIRV',
            'SDL_ShaderCross_CompileDXBCFromSPIRV',
            'SDL_ShaderCross_CompileGraphicsShaderFromSPIRV',
            'SDL_ShaderCross_ReflectGraphicsSPIRV'
        ]
        
        for func in shadercross_functions:
            if self.test_function_exists('', func):
                self.add_result(TestCase(
                    f"SDL3_shadercross - {func}",
                    f"Function {func} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_shadercross - {func}",
                    f"Function {func} missing",
                    TestResult.FAIL
                ))
        
        # Test ShaderCross structures
        shadercross_structures = [
            'SDL_ShaderCross_SPIRV_Info', 'SDL_ShaderCross_HLSL_Info',
            'SDL_ShaderCross_GraphicsShaderMetadata', 'SDL_ShaderCross_ComputePipelineMetadata'
        ]
        
        for struct in shadercross_structures:
            if self.test_structure_exists(struct):
                self.add_result(TestCase(
                    f"SDL3_shadercross - {struct}",
                    f"Structure {struct} exists",
                    TestResult.PASS
                ))
            else:
                self.add_result(TestCase(
                    f"SDL3_shadercross - {struct}",
                    f"Structure {struct} missing",
                    TestResult.FAIL
                ))

    def test_functional_integration(self):
        """Test basic functional integration."""
        print("🔬 Testing Functional Integration...")
        
        try:
            # Test basic SDL initialization
            if hasattr(sdl3, 'SDL_Init') and hasattr(sdl3, 'SDL_INIT_VIDEO'):
                result = sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO)
                if result:
                    self.add_result(TestCase(
                        "Integration - SDL_Init",
                        "SDL initialization successful",
                        TestResult.PASS
                    ))
                    
                    # Test basic error handling
                    if hasattr(sdl3, 'SDL_GetError'):
                        error = sdl3.SDL_GetError()
                        self.add_result(TestCase(
                            "Integration - Error Handling",
                            "Error function callable",
                            TestResult.PASS
                        ))
                    
                    # Cleanup
                    if hasattr(sdl3, 'SDL_Quit'):
                        sdl3.SDL_Quit()
                        self.add_result(TestCase(
                            "Integration - SDL_Quit",
                            "SDL cleanup successful",
                            TestResult.PASS
                        ))
                else:
                    self.add_result(TestCase(
                        "Integration - SDL_Init",
                        "SDL initialization failed",
                        TestResult.FAIL
                    ))
            else:
                self.add_result(TestCase(
                    "Integration - SDL_Init",
                    "SDL_Init or SDL_INIT_VIDEO not available",
                    TestResult.FAIL
                ))
                
        except Exception as e:
            self.add_result(TestCase(
                "Integration - Basic Test",
                "Integration test failed",
                TestResult.FAIL,
                error=str(e)
            ))

    def test_ctypes_integration(self):
        """Test ctypes integration and type system."""
        print("🔍 Testing ctypes Integration...")
        
        # Test if SDL_POINTER wrapper exists
        try:
            from sdl3 import SDL_POINTER
            self.add_result(TestCase(
                "ctypes - SDL_POINTER",
                "SDL_POINTER wrapper exists",
                TestResult.PASS
            ))
        except ImportError:
            self.add_result(TestCase(
                "ctypes - SDL_POINTER", 
                "SDL_POINTER wrapper missing",
                TestResult.FAIL
            ))
        
        # Test if SDL_FUNC wrapper exists
        try:
            from sdl3 import SDL_FUNC
            self.add_result(TestCase(
                "ctypes - SDL_FUNC",
                "SDL_FUNC wrapper exists", 
                TestResult.PASS
            ))
        except ImportError:
            self.add_result(TestCase(
                "ctypes - SDL_FUNC",
                "SDL_FUNC wrapper missing",
                TestResult.FAIL
            ))

    def run_all_tests(self):
        """Run the complete test suite."""
        print("=" * 60)
        print("🧪 PySDL3 Coverage Evaluation Test Suite")
        print("=" * 60)
        print()
        
        # Run all test categories
        test_methods = [
            self.test_ctypes_integration,
            self.test_sdl3_core,
            self.test_sdl3_video,
            self.test_sdl3_audio,
            self.test_sdl3_image,
            self.test_sdl3_mixer,
            self.test_sdl3_ttf,
            self.test_sdl3_net,
            self.test_sdl3_rtf,
            self.test_sdl3_shadercross,
            self.test_functional_integration
        ]
        
        for test_method in test_methods:
            try:
                test_method()
            except Exception as e:
                self.add_result(TestCase(
                    f"ERROR - {test_method.__name__}",
                    "Test method crashed",
                    TestResult.FAIL,
                    error=str(e)
                ))
            print()

    def print_results(self):
        """Print detailed test results."""
        print("=" * 60)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 60)
        
        # Print statistics
        total_tests = len(self.results)
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {self.stats[TestResult.PASS]} ({self.stats[TestResult.PASS]/total_tests*100:.1f}%)")
        print(f"❌ Failed: {self.stats[TestResult.FAIL]} ({self.stats[TestResult.FAIL]/total_tests*100:.1f}%)")
        print(f"⚠️  Warnings: {self.stats[TestResult.WARN]} ({self.stats[TestResult.WARN]/total_tests*100:.1f}%)")
        print(f"⏭️  Skipped: {self.stats[TestResult.SKIP]} ({self.stats[TestResult.SKIP]/total_tests*100:.1f}%)")
        print()
        
        # Print coverage assessment
        pass_rate = self.stats[TestResult.PASS] / total_tests * 100
        if pass_rate >= 90:
            coverage_rating = "🏆 EXCELLENT"
        elif pass_rate >= 75:
            coverage_rating = "✅ GOOD"
        elif pass_rate >= 60:
            coverage_rating = "⚠️ FAIR"
        else:
            coverage_rating = "❌ POOR"
        
        print(f"Overall Coverage Rating: {coverage_rating} ({pass_rate:.1f}%)")
        print()
        
        # Print detailed results grouped by category
        categories = {}
        for result in self.results:
            category = result.name.split(' - ')[0] if ' - ' in result.name else 'General'
            if category not in categories:
                categories[category] = []
            categories[category].append(result)
        
        print("=" * 60)
        print("📋 DETAILED RESULTS BY CATEGORY")
        print("=" * 60)
        
        for category, tests in sorted(categories.items()):
            print(f"\n🔸 {category}")
            print("-" * 40)
            
            category_stats = {TestResult.PASS: 0, TestResult.FAIL: 0, TestResult.WARN: 0, TestResult.SKIP: 0}
            for test in tests:
                category_stats[test.result] += 1
                status = test.result.value
                print(f"  {status} {test.description}")
                if test.error:
                    print(f"     Error: {test.error}")
            
            category_total = len(tests)
            category_pass_rate = category_stats[TestResult.PASS] / category_total * 100
            print(f"  📈 Category Coverage: {category_pass_rate:.1f}% ({category_stats[TestResult.PASS]}/{category_total})")
        
        # Print failed tests for debugging
        failed_tests = [test for test in self.results if test.result == TestResult.FAIL]
        if failed_tests:
            print("\n" + "=" * 60)
            print("🔍 FAILED TESTS (for debugging)")
            print("=" * 60)
            for test in failed_tests:
                print(f"❌ {test.name}: {test.description}")
                if test.error:
                    print(f"   Error: {test.error}")

@TEST_RegisterFunction(["Darwin", "Windows", "Linux"])
def TEST_PySDL3_Coverage_Evaluation():
    """PySDL3 comprehensive coverage evaluation test."""
    print("🧪 PySDL3 Coverage Evaluation Test Suite")
    print("=" * 60)
    print()
    
    # Create and run test suite
    test_suite = PySDL3CoverageTest()
    test_suite.run_all_tests()
    test_suite.print_results()
    
    # Assert based on results - fail if too many tests fail
    total_tests = len(test_suite.results)
    failed_tests = test_suite.stats[TestResult.FAIL]
    
    if total_tests == 0:
        assert False, "No tests were executed"
    
    # Allow up to 20% failure rate for a passing test
    failure_rate = failed_tests / total_tests
    assert failure_rate <= 0.2, f"Too many tests failed: {failed_tests}/{total_tests} ({failure_rate*100:.1f}%)"
    
    print("✅ Coverage evaluation test passed!")

def main():
    """Main test execution function - for standalone execution."""
    print("Starting PySDL3 Coverage Evaluation...")
    print(f"Python version: {sys.version}")
    print(f"Test date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create and run test suite
    test_suite = PySDL3CoverageTest()
    test_suite.run_all_tests()
    test_suite.print_results()
    
    # Return exit code based on results
    if test_suite.stats[TestResult.FAIL] == 0:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️ {test_suite.stats[TestResult.FAIL]} test(s) failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
