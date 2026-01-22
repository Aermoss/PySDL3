#!/usr/bin/env python3
"""
PySDL3 Custom Libraries Setup

This utility helps configure PySDL3 to use custom compiled SDL3 binaries.
It includes both setup functionality and usage examples.

Usage:
    python3 custom_libraries_setup.py /path/to/custom/libraries [--env-vars] [--example]
    
Examples:
    # Set up with metadata file (recommended)
    python3 custom_libraries_setup.py /usr/local/lib64
    
    # Set up with environment variables
    python3 custom_libraries_setup.py /usr/local/lib64 --env-vars
    
    # Set up and run example
    python3 custom_libraries_setup.py /usr/local/lib64 --example
    
    # Just run example (requires existing setup)
    python3 custom_libraries_setup.py --example-only
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional

class CustomLibrariesSetup:
    """Utility class for setting up PySDL3 with custom libraries."""
    
    def __init__(self, custom_binaries_path: str, pysdl3_path: Optional[str] = None):
        if pysdl3_path is None:
            pysdl3_path = str(Path(__file__).parent)
            
        self.custom_binaries_path = Path(custom_binaries_path)
        self.pysdl3_path = Path(pysdl3_path)
        self.pysdl3_bin_path = self.pysdl3_path / "sdl3" / "bin"
        
        # SDL3 modules to look for
        self.sdl_modules = [
            "SDL3", "SDL3_image", "SDL3_mixer", 
            "SDL3_ttf", "SDL3_rtf", "SDL3_net", "SDL3_shadercross"
        ]
    
    def find_custom_libraries(self) -> Dict[str, str]:
        """Find SDL3 libraries in the custom binaries path."""
        if not self.custom_binaries_path.exists():
            print(f"ERROR: Custom binaries path does not exist: {self.custom_binaries_path}")
            return {}
        
        found_libraries = {}
        static_only_libraries = []
        
        for module in self.sdl_modules:
            # Look for various library file patterns
            lib_patterns = [
                f"lib{module}.so",           # Standard shared library
                f"lib{module}.so.0",         # Versioned shared library  
                f"{module}.so",              # Alternative naming
            ]
            
            found_shared = False
            for pattern in lib_patterns:
                lib_path = self.custom_binaries_path / pattern
                if lib_path.exists():
                    found_libraries[module] = str(lib_path)
                    found_shared = True
                    break
            
            # If no shared library found, check for static library
            if not found_shared:
                static_patterns = [
                    f"lib{module}.a",        # Static library
                ]
                
                for pattern in static_patterns:
                    lib_path = self.custom_binaries_path / pattern
                    if lib_path.exists():
                        static_only_libraries.append(module)
                        break
        
        # Report static-only libraries
        if static_only_libraries:
            print(f"Note: Found static-only libraries (not loadable by PySDL3): {', '.join(static_only_libraries)}")
        
        return found_libraries
    
    def create_metadata(self, libraries: Dict[str, str]) -> bool:
        """Create metadata.json file for PySDL3."""
        if not libraries:
            print("No libraries found to create metadata for.")
            return False
        
        # Create metadata structure
        metadata = {
            "arch": "AMD64",
            "system": "Linux",
            "target": "v0.9.8",  # Compatible with current PySDL3 version
            "version": "custom-build",
            "url": "local",
            "created": "custom",
            "updated": "custom",
            "uploader": "local",
            "files": list(libraries.values()),
            "repair": False,
            "find": True  # Allow fallback to system libraries
        }
        
        # Ensure bin directory exists
        self.pysdl3_bin_path.mkdir(parents=True, exist_ok=True)
        
        # Write metadata file
        metadata_path = self.pysdl3_bin_path / "metadata.json"
        try:
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"✓ Created metadata: {metadata_path}")
            return True
            
        except Exception as e:
            print(f"✗ Failed to create metadata: {e}")
            return False
    
    def setup_environment_variables(self):
        """Set up environment variables for PySDL3."""
        os.environ["SDL_BINARY_PATH"] = str(self.custom_binaries_path)
        os.environ["SDL_DOWNLOAD_BINARIES"] = "0"  # Don't download binaries
        os.environ["SDL_FIND_BINARIES"] = "1"      # Find system libraries as fallback
        
        print("Environment variables configured:")
        print(f"  SDL_BINARY_PATH = {os.environ['SDL_BINARY_PATH']}")
        print(f"  SDL_DOWNLOAD_BINARIES = {os.environ['SDL_DOWNLOAD_BINARIES']}")
        print(f"  SDL_FIND_BINARIES = {os.environ['SDL_FIND_BINARIES']}")
    
    def setup(self, use_env_vars: bool = False) -> bool:
        """
        Set up PySDL3 to use custom libraries.
        
        Args:
            use_env_vars: If True, use environment variables instead of metadata file
            
        Returns:
            True if setup was successful
        """
        print("PySDL3 Custom Libraries Setup")
        print("=" * 40)
        print(f"Custom binaries: {self.custom_binaries_path}")
        print(f"PySDL3 path: {self.pysdl3_path}")
        print()
        
        # Find libraries
        libraries = self.find_custom_libraries()
        
        if not libraries:
            print("No SDL3 libraries found in custom path!")
            return False
        
        print("Found libraries:")
        for module, path in libraries.items():
            print(f"  ✓ {module}: {path}")
        print()
        
        if use_env_vars:
            # Use environment variables approach
            self.setup_environment_variables()
            return True
        else:
            # Use metadata file approach
            return self.create_metadata(libraries)
    
    def verify_setup(self) -> bool:
        """Verify that PySDL3 can load with the custom libraries."""
        print("Verifying setup...")
        
        # Add PySDL3 to path
        if str(self.pysdl3_path) not in sys.path:
            sys.path.insert(0, str(self.pysdl3_path))
        
        try:
            import sdl3
            print(f"✓ PySDL3 imported successfully (version: {sdl3.__version__})")
            
            # Check loaded binaries
            if hasattr(sdl3, 'binaryMap') and sdl3.binaryMap:
                loaded_count = len([k for k, v in sdl3.binaryMap.items() if v])
                print(f"✓ Loaded {loaded_count} binaries")
                
                for module, binary in sdl3.binaryMap.items():
                    if binary:
                        try:
                            path = getattr(binary, '_name', '<unknown>')
                            print(f"  ✓ {module}: {path}")
                        except:
                            print(f"  ✓ {module}: <loaded>")
                
                return True
            else:
                print("✗ No binaries loaded")
                return False
                
        except ImportError as e:
            print(f"✗ Failed to import PySDL3: {e}")
            return False
        except Exception as e:
            print(f"✗ Error verifying setup: {e}")
            return False
    
    def run_example(self) -> bool:
        """Run example demonstrating PySDL3 with custom libraries."""
        print("\nRunning PySDL3 Example with Custom Libraries")
        print("=" * 50)
        
        # Add PySDL3 to path
        if str(self.pysdl3_path) not in sys.path:
            sys.path.insert(0, str(self.pysdl3_path))
        
        try:
            import sdl3
            
            # Initialize SDL3
            if sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO) == 0:
                print("✓ SDL3 initialized successfully")
                
                # Get version info
                version = sdl3.SDL_Version()
                sdl3.SDL_GetVersion(version)
                print(f"✓ SDL3 Version: {version.major}.{version.minor}.{version.patch}")
                
                # Test window creation
                window = sdl3.SDL_CreateWindow(
                    b"PySDL3 Custom Libraries Example",
                    800, 600,
                    sdl3.SDL_WINDOW_RESIZABLE
                )
                
                if window:
                    print("✓ Window created successfully")
                    
                    # Test other libraries
                    available_libs = []
                    if 'SDL3_image' in sdl3.binaryMap and sdl3.binaryMap['SDL3_image']:
                        available_libs.append("SDL3_image")
                    
                    if 'SDL3_mixer' in sdl3.binaryMap and sdl3.binaryMap['SDL3_mixer']:
                        available_libs.append("SDL3_mixer")
                        
                    if 'SDL3_ttf' in sdl3.binaryMap and sdl3.binaryMap['SDL3_ttf']:
                        available_libs.append("SDL3_ttf")
                    
                    if 'SDL3_net' in sdl3.binaryMap and sdl3.binaryMap['SDL3_net']:
                        available_libs.append("SDL3_net")
                    
                    if available_libs:
                        print(f"✓ Additional libraries available: {', '.join(available_libs)}")
                    
                    # Simple event loop for demonstration
                    print("✓ Running simple event loop (press close button to exit)...")
                    
                    running = True
                    event = sdl3.SDL_Event()
                    
                    # Run for a short time or until window is closed
                    import time
                    start_time = time.time()
                    
                    while running and (time.time() - start_time) < 3.0:  # Run for 3 seconds max
                        while sdl3.SDL_PollEvent(event):
                            if event.type == sdl3.SDL_EVENT_QUIT:
                                running = False
                                break
                        
                        # Simple delay
                        sdl3.SDL_Delay(16)  # ~60 FPS
                    
                    print("✓ Event loop completed")
                    
                    # Clean up
                    sdl3.SDL_DestroyWindow(window)
                    print("✓ Window destroyed")
                else:
                    print("✗ Failed to create window")
                    return False
                
                # Clean up SDL3
                sdl3.SDL_Quit()
                print("✓ SDL3 quit successfully")
                
                print("\n🎉 Custom libraries example completed successfully!")
                return True
            else:
                error = sdl3.SDL_GetError()
                if error:
                    error_msg = error.decode() if hasattr(error, 'decode') else str(error)
                    print(f"✗ Failed to initialize SDL3: {error_msg}")
                else:
                    print("✗ Failed to initialize SDL3")
                return False
                
        except Exception as e:
            print(f"✗ Error running example: {e}")
            import traceback
            traceback.print_exc()
            return False

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Set up PySDL3 to use custom compiled SDL3 libraries",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "custom_path",
        nargs='?',
        help="Path to custom compiled SDL3 binaries"
    )
    parser.add_argument(
        "--pysdl3-path", 
        default=str(Path(__file__).parent),
        help="Path to PySDL3 installation (default: current directory)"
    )
    parser.add_argument(
        "--env-vars", 
        action="store_true",
        help="Use environment variables instead of metadata file"
    )
    parser.add_argument(
        "--example",
        action="store_true", 
        help="Run example after setup"
    )
    parser.add_argument(
        "--example-only",
        action="store_true",
        help="Only run example (requires existing setup)"
    )
    parser.add_argument(
        "--verify-only",
        action="store_true", 
        help="Only verify existing setup, don't modify"
    )
    
    args = parser.parse_args()
    
    # Handle example-only case
    if args.example_only:
        if not args.custom_path:
            # Try to find existing metadata
            pysdl3_path = Path(args.pysdl3_path)
            metadata_path = pysdl3_path / "sdl3" / "bin" / "metadata.json"
            if metadata_path.exists():
                try:
                    with open(metadata_path) as f:
                        metadata = json.load(f)
                    if metadata.get("files"):
                        # Use the first library's directory as custom path
                        first_lib = Path(metadata["files"][0])
                        args.custom_path = str(first_lib.parent)
                except:
                    pass
        
        if not args.custom_path:
            print("ERROR: --example-only requires either existing metadata or custom_path argument")
            sys.exit(1)
        
        setup = CustomLibrariesSetup(args.custom_path, args.pysdl3_path)
        success = setup.run_example()
        sys.exit(0 if success else 1)
    
    # Validate arguments
    if not args.custom_path:
        parser.error("custom_path is required (unless using --example-only)")
    
    setup = CustomLibrariesSetup(args.custom_path, args.pysdl3_path)
    
    if args.verify_only:
        success = setup.verify_setup()
    else:
        success = setup.setup(args.env_vars)
        if success:
            success = setup.verify_setup()
            
        if success and args.example:
            setup.run_example()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
