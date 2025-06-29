#!/usr/bin/env python3
"""
PySDL3 Custom Libraries Test Suite

This test suite validates that PySDL3 can work with custom compiled SDL3 binaries.
It includes configuration validation and functionality tests.

Usage:
    python3 tests/TEST_custom_libraries.py /path/to/custom/libraries [/path/to/pysdl3]
"""

import os
import sys
import json
import ctypes
import ctypes.util
from pathlib import Path
from typing import Dict, List, Optional

class CustomLibrariesTest:
    """Test suite for PySDL3 custom libraries configuration."""
    
    def __init__(self, custom_binaries_path: str, pysdl3_path: str):
        self.custom_binaries_path = custom_binaries_path
        self.pysdl3_path = pysdl3_path
        self.pysdl3_bin_path = os.path.join(pysdl3_path, "sdl3", "bin")
        self.test_results = []
        
        # Expected SDL3 modules
        self.sdl_modules = [
            "SDL3", "SDL3_image", "SDL3_mixer", 
            "SDL3_ttf", "SDL3_rtf", "SDL3_net", "SDL3_shadercross"
        ]
    
    def log(self, test_name: str, success: bool, message: str):
        """Log test results."""
        status = "✓" if success else "✗"
        print(f"  {status} {test_name}: {message}")
        self.test_results.append({
            "test": test_name,
            "success": success,
            "message": message
        })
    
    def test_custom_binaries_exist(self) -> bool:
        """Test 1: Check if custom binaries directory and files exist."""
        print("Test 1: Custom Binaries Existence")
        
        if not os.path.exists(self.custom_binaries_path):
            self.log("Directory Check", False, f"Path does not exist: {self.custom_binaries_path}")
            return False
        
        self.log("Directory Check", True, f"Path exists: {self.custom_binaries_path}")
        
        # Check for SDL3 libraries
        found_libs = []
        expected_libs = ["libSDL3.so", "libSDL3_image.so", "libSDL3_mixer.so", "libSDL3_ttf.so", "libSDL3_net.so"]
        
        for lib in expected_libs:
            lib_path = os.path.join(self.custom_binaries_path, lib)
            if os.path.exists(lib_path):
                found_libs.append(lib)
                self.log("Library Check", True, f"Found {lib}")
            else:
                self.log("Library Check", False, f"Missing {lib}")
        
        success = len(found_libs) > 0
        return success
    
    def test_ctypes_library_loading(self) -> bool:
        """Test 2: Test direct ctypes library loading."""
        print("\nTest 2: Direct Library Loading")
        
        success_count = 0
        expected_libs = ["libSDL3.so", "libSDL3_image.so", "libSDL3_mixer.so", "libSDL3_ttf.so", "libSDL3_net.so"]
        
        for lib in expected_libs:
            lib_path = os.path.join(self.custom_binaries_path, lib)
            if os.path.exists(lib_path):
                try:
                    dll = ctypes.CDLL(lib_path)
                    self.log("Direct Loading", True, f"Successfully loaded {lib}")
                    success_count += 1
                except Exception as e:
                    self.log("Direct Loading", False, f"Failed to load {lib}: {e}")
            else:
                self.log("Direct Loading", False, f"File not found: {lib}")
        
        return success_count > 0
    
    def test_find_library_detection(self) -> bool:
        """Test 3: Test ctypes.util.find_library detection."""
        print("\nTest 3: System Library Detection")
        
        found_count = 0
        for module in ["SDL3", "SDL3_image", "SDL3_mixer", "SDL3_ttf", "SDL3_net"]:
            found = ctypes.util.find_library(module)
            if found:
                self.log("Find Library", True, f"{module}: {found}")
                found_count += 1
            else:
                self.log("Find Library", False, f"{module}: Not found in system")
        
        return found_count > 0
    
    def setup_metadata(self) -> bool:
        """Test 4: Setup PySDL3 metadata for custom libraries."""
        print("\nTest 4: Metadata Setup")
        
        # Find available libraries
        libraries = {}
        for module in self.sdl_modules:
            lib_patterns = [
                f"lib{module}.so",
                f"lib{module}.so.0",
                f"{module}.so",
            ]
            
            for pattern in lib_patterns:
                lib_path = os.path.join(self.custom_binaries_path, pattern)
                if os.path.exists(lib_path):
                    libraries[module] = lib_path
                    break
        
        if not libraries:
            self.log("Library Discovery", False, "No SDL3 libraries found")
            return False
        
        self.log("Library Discovery", True, f"Found {len(libraries)} libraries")
        
        # Create metadata
        metadata = {
            "arch": "AMD64",
            "system": "Linux", 
            "target": "v0.9.8",
            "version": "custom-build",
            "url": "local",
            "created": "custom",
            "updated": "custom",
            "uploader": "local",
            "files": list(libraries.values()),
            "repair": False,
            "find": True
        }
        
        # Write metadata
        try:
            os.makedirs(self.pysdl3_bin_path, exist_ok=True)
            metadata_path = os.path.join(self.pysdl3_bin_path, "metadata.json")
            
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            self.log("Metadata Creation", True, f"Created {metadata_path}")
            return True
            
        except Exception as e:
            self.log("Metadata Creation", False, f"Failed to create metadata: {e}")
            return False
    
    def test_pysdl3_import(self) -> bool:
        """Test 5: Test PySDL3 import with custom libraries."""
        print("\nTest 5: PySDL3 Import Test")
        
        # Set environment variables
        os.environ["SDL_DOWNLOAD_BINARIES"] = "0"
        os.environ["SDL_DEBUG"] = "1"
        os.environ["SDL_LOG_LEVEL"] = "0"
        
        # Add PySDL3 to path
        if self.pysdl3_path not in sys.path:
            sys.path.insert(0, self.pysdl3_path)
        
        try:
            import sdl3
            self.log("PySDL3 Import", True, f"Successfully imported PySDL3 v{sdl3.__version__}")
            
            # Check binary mappings
            if hasattr(sdl3, 'binaryMap') and sdl3.binaryMap:
                loaded_count = len([k for k, v in sdl3.binaryMap.items() if v])
                self.log("Binary Loading", True, f"Loaded {loaded_count} binaries")
                
                # Log which binaries were loaded
                for module, binary in sdl3.binaryMap.items():
                    if binary:
                        try:
                            path = getattr(binary, '_name', '<unknown>')
                            self.log("Binary Mapping", True, f"{module}: {path}")
                        except:
                            self.log("Binary Mapping", True, f"{module}: <loaded>")
                
                return loaded_count > 0
            else:
                self.log("Binary Loading", False, "No binaries loaded")
                return False
                
        except ImportError as e:
            self.log("PySDL3 Import", False, f"Import failed: {e}")
            return False
        except Exception as e:
            self.log("PySDL3 Import", False, f"Error: {e}")
            return False
    
    def test_sdl3_functionality(self) -> bool:
        """Test 6: Test basic SDL3 functionality."""
        print("\nTest 6: SDL3 Functionality Test")
        
        try:
            import sdl3
            
            # Test SDL_Init
            if hasattr(sdl3, 'SDL_Init') and hasattr(sdl3, 'SDL_INIT_VIDEO'):
                init_result = sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO)
                if init_result == 0:
                    self.log("SDL_Init", True, "SDL3 initialized successfully")
                    
                    # Test version info
                    if hasattr(sdl3, 'SDL_Version') and hasattr(sdl3, 'SDL_GetVersion'):
                        try:
                            version = sdl3.SDL_Version()
                            sdl3.SDL_GetVersion(version)
                            version_str = f"{version.major}.{version.minor}.{version.patch}"
                            self.log("Version Check", True, f"SDL3 version: {version_str}")
                        except:
                            self.log("Version Check", False, "Could not get SDL3 version")
                    
                    # Test window creation
                    if hasattr(sdl3, 'SDL_CreateWindow') and hasattr(sdl3, 'SDL_WINDOW_RESIZABLE'):
                        try:
                            window = sdl3.SDL_CreateWindow(
                                b"PySDL3 Test",
                                640, 480,
                                sdl3.SDL_WINDOW_RESIZABLE
                            )
                            
                            if window:
                                self.log("Window Creation", True, "Window created successfully")
                                
                                # Clean up window
                                if hasattr(sdl3, 'SDL_DestroyWindow'):
                                    sdl3.SDL_DestroyWindow(window)
                                    self.log("Window Cleanup", True, "Window destroyed")
                            else:
                                self.log("Window Creation", False, "Failed to create window")
                        except Exception as e:
                            self.log("Window Creation", False, f"Window creation failed: {e}")
                    
                    # Clean up SDL
                    if hasattr(sdl3, 'SDL_Quit'):
                        sdl3.SDL_Quit()
                        self.log("SDL_Quit", True, "SDL3 quit successfully")
                    
                    return True
                else:
                    self.log("SDL_Init", False, f"SDL_Init failed with code: {init_result}")
                    return False
            else:
                self.log("SDL Functions", False, "SDL_Init or SDL_INIT_VIDEO not available")
                return False
                
        except Exception as e:
            self.log("SDL3 Functionality", False, f"Error testing functionality: {e}")
            return False
    
    def run_all_tests(self) -> bool:
        """Run all tests and return overall success."""
        print("PySDL3 Custom Libraries Test Suite")
        print("=" * 50)
        print(f"Custom binaries path: {self.custom_binaries_path}")
        print(f"PySDL3 path: {self.pysdl3_path}")
        print()
        
        tests = [
            self.test_custom_binaries_exist,
            self.test_ctypes_library_loading,
            self.test_find_library_detection,
            self.setup_metadata,
            self.test_pysdl3_import,
            self.test_sdl3_functionality
        ]
        
        passed = 0
        for test in tests:
            try:
                if test():
                    passed += 1
            except Exception as e:
                print(f"Test failed with exception: {e}")
        
        print(f"\nTest Results: {passed}/{len(tests)} tests passed")
        
        # Summary
        success_count = len([r for r in self.test_results if r["success"]])
        total_count = len(self.test_results)
        
        print(f"Individual checks: {success_count}/{total_count} passed")
        
        if passed == len(tests):
            print("\n🎉 All tests passed! PySDL3 is working with your custom binaries!")
        elif passed > 0:
            print("\n⚠️  Some tests passed. PySDL3 may work partially with your custom binaries.")
        else:
            print("\n❌ All tests failed. PySDL3 configuration needs attention.")
        
        return passed == len(tests)

def main():
    """Main test runner."""
    # Default paths - adjust as needed
    custom_binaries_path = "/home/thyne/VSCodeProjects/testengine3/deps/install/lib64"
    pysdl3_path = "/home/thyne/VSCodeProjects/testengine3/ext/PySDL3"
    
    # Allow path override via command line
    if len(sys.argv) >= 2:
        custom_binaries_path = sys.argv[1]
    if len(sys.argv) >= 3:
        pysdl3_path = sys.argv[2]
    
    # Run tests
    test_suite = CustomLibrariesTest(custom_binaries_path, pysdl3_path)
    success = test_suite.run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
