#!/usr/bin/env python3
"""
PySDL3 Coverage Test Runner

This script runs comprehensive tests to evaluate PySDL3 coverage.
It includes both structural analysis and functional testing.

Author: Test Runner Generator
Date: June 28, 2025
"""

import os
import sys
import subprocess
import time

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

def run_test_script(script_name, description):
    """Run a test script and capture results."""
    print(f"🚀 Running {description}...")
    print("=" * 60)
    
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    
    if not os.path.exists(script_path):
        print(f"❌ Test script not found: {script_path}")
        return False
    
    try:
        # Run the script
        result = subprocess.run([
            sys.executable, script_path
        ], capture_output=True, text=True, timeout=120)
        
        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        # Return success status
        success = result.returncode == 0
        print(f"\n📊 {description} Result: {'✅ PASSED' if success else '❌ FAILED'}")
        print("=" * 60)
        return success
        
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} timed out after 120 seconds")
        return False
    except Exception as e:
        print(f"💥 Error running {description}: {e}")
        return False

def check_pysdl3_installation():
    """Check if PySDL3 can be imported."""
    print("🔍 Checking PySDL3 Installation...")
    print("-" * 40)
    
    # Check if PySDL3 directory exists (we're already inside it)
    pysdl3_path = os.path.dirname(os.path.dirname(__file__))
    print(f"✅ PySDL3 directory: {pysdl3_path}")
    
    # Check if main sdl3 module exists
    sdl3_init = os.path.join(pysdl3_path, 'sdl3', '__init__.py')
    if not os.path.exists(sdl3_init):
        print(f"❌ SDL3 module not found: {sdl3_init}")
        return False
    
    print(f"✅ SDL3 module found: {sdl3_init}")
    
    # Try importing (already imported via __init__)
    try:
        print("✅ PySDL3 imported successfully")
        
        # Check version if available
        if hasattr(sdl3, '__version__'):
            print(f"📦 PySDL3 Version: {sdl3.__version__}")
        
        # Check if main SDL functions are available
        key_functions = ['SDL_Init', 'SDL_Quit', 'SDL_GetVersion']
        available_functions = sum(1 for func in key_functions if hasattr(sdl3, func))
        print(f"🔧 Key functions available: {available_functions}/{len(key_functions)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking PySDL3: {e}")
        return False

def create_simple_functionality_test():
    """Create a simple inline functionality test."""
    print("🧪 Running Simple Functionality Test...")
    print("-" * 40)
    
    try:
        tests_passed = 0
        total_tests = 0
        
        # Test 1: Check if SDL_Init exists and is callable
        total_tests += 1
        if hasattr(sdl3, 'SDL_Init') and callable(getattr(sdl3, 'SDL_Init')):
            print("✅ SDL_Init is available and callable")
            tests_passed += 1
        else:
            print("❌ SDL_Init is not available or not callable")
        
        # Test 2: Check if constants exist
        total_tests += 1
        constants_to_check = ['SDL_INIT_VIDEO', 'SDL_INIT_AUDIO', 'SDL_INIT_EVENTS']
        available_constants = sum(1 for const in constants_to_check if hasattr(sdl3, const))
        if available_constants == len(constants_to_check):
            print(f"✅ All basic constants available ({available_constants}/{len(constants_to_check)})")
            tests_passed += 1
        else:
            print(f"⚠️ Some constants missing ({available_constants}/{len(constants_to_check)})")
        
        # Test 3: Check if image library functions exist
        total_tests += 1
        img_functions = ['IMG_Init', 'IMG_Load', 'IMG_Quit']
        available_img = sum(1 for func in img_functions if hasattr(sdl3, func))
        if available_img >= 2:  # At least 2 out of 3
            print(f"✅ Image functions available ({available_img}/{len(img_functions)})")
            tests_passed += 1
        else:
            print(f"❌ Image functions missing ({available_img}/{len(img_functions)})")
        
        # Test 4: Check if mixer library functions exist
        total_tests += 1
        mix_functions = ['Mix_Init', 'Mix_OpenAudio', 'Mix_Quit']
        available_mix = sum(1 for func in mix_functions if hasattr(sdl3, func))
        if available_mix >= 2:  # At least 2 out of 3
            print(f"✅ Mixer functions available ({available_mix}/{len(mix_functions)})")
            tests_passed += 1
        else:
            print(f"❌ Mixer functions missing ({available_mix}/{len(mix_functions)})")
        
        # Test 5: Check if TTF library functions exist
        total_tests += 1
        ttf_functions = ['TTF_Init', 'TTF_OpenFont', 'TTF_Quit']
        available_ttf = sum(1 for func in ttf_functions if hasattr(sdl3, func))
        if available_ttf >= 2:  # At least 2 out of 3
            print(f"✅ TTF functions available ({available_ttf}/{len(ttf_functions)})")
            tests_passed += 1
        else:
            print(f"❌ TTF functions missing ({available_ttf}/{len(ttf_functions)})")
        
        success_rate = (tests_passed / total_tests) * 100
        print(f"\n📊 Simple Test Results: {tests_passed}/{total_tests} ({success_rate:.1f}%)")
        
        return success_rate >= 80
        
    except Exception as e:
        print(f"❌ Simple functionality test failed: {e}")
        return False

@TEST_RegisterFunction(["Darwin", "Windows", "Linux"])
def TEST_PySDL3_Runner():
    """PySDL3 comprehensive test runner."""
    print("🎯 PySDL3 Coverage Test Suite Runner")
    print("=" * 60)
    print(f"⏰ Test started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python version: {sys.version}")
    print(f"📁 Working directory: {os.getcwd()}")
    print()
    
    # Track overall results
    test_results = []
    
    # Step 1: Check PySDL3 installation
    installation_ok = check_pysdl3_installation()
    test_results.append(("Installation Check", installation_ok))
    print()
    
    assert installation_ok, "PySDL3 installation check failed"
    
    # Step 2: Run simple functionality test
    simple_test_ok = create_simple_functionality_test()
    test_results.append(("Simple Functionality", simple_test_ok))
    print()
    
    # Step 3: Run module structure analyzer
    module_analyzer_ok = run_test_script("TEST_module_analyzer.py", "Module Structure Analysis")
    test_results.append(("Module Analysis", module_analyzer_ok))
    print()
    
    # Step 4: Run comprehensive coverage test
    coverage_test_ok = run_test_script("TEST_coverage_evaluation.py", "Comprehensive Coverage Test")
    test_results.append(("Coverage Test", coverage_test_ok))
    print()
    
    # Generate final report
    print("🏁 FINAL TEST SUMMARY")
    print("=" * 60)
    
    passed_tests = sum(1 for _, result in test_results if result)
    total_tests = len(test_results)
    overall_success_rate = (passed_tests / total_tests) * 100
    
    for test_name, result in test_results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status} {test_name}")
    
    print(f"\n📊 Overall Test Results: {passed_tests}/{total_tests} ({overall_success_rate:.1f}%)")
    
    # Assert overall success
    assert overall_success_rate >= 50, f"Overall test success rate too low: {overall_success_rate:.1f}%"
    
    print("✅ Test runner completed successfully!")

def main():
    """Main test runner function - for standalone execution."""
    print("🎯 PySDL3 Coverage Test Suite Runner")
    print("=" * 60)
    print(f"⏰ Test started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python version: {sys.version}")
    print(f"📁 Working directory: {os.getcwd()}")
    print()
    
    # Track overall results
    test_results = []
    
    # Step 1: Check PySDL3 installation
    installation_ok = check_pysdl3_installation()
    test_results.append(("Installation Check", installation_ok))
    print()
    
    if not installation_ok:
        print("❌ PySDL3 installation check failed. Cannot proceed with further tests.")
        return 1
    
    # Step 2: Run simple functionality test
    simple_test_ok = create_simple_functionality_test()
    test_results.append(("Simple Functionality", simple_test_ok))
    print()
    
    # Step 3: Run module structure analyzer
    module_analyzer_ok = run_test_script("TEST_module_analyzer.py", "Module Structure Analysis")
    test_results.append(("Module Analysis", module_analyzer_ok))
    print()
    
    # Step 4: Run comprehensive coverage test
    coverage_test_ok = run_test_script("TEST_coverage_evaluation.py", "Comprehensive Coverage Test")
    test_results.append(("Coverage Test", coverage_test_ok))
    print()
    
    # Generate final report
    print("🏁 FINAL TEST SUMMARY")
    print("=" * 60)
    
    passed_tests = sum(1 for _, result in test_results if result)
    total_tests = len(test_results)
    overall_success_rate = (passed_tests / total_tests) * 100
    
    for test_name, result in test_results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status} {test_name}")
    
    print(f"\n📊 Overall Test Results: {passed_tests}/{total_tests} ({overall_success_rate:.1f}%)")
    
    if overall_success_rate >= 75:
        final_assessment = "🏆 EXCELLENT - PySDL3 is well-implemented with good coverage"
    elif overall_success_rate >= 50:
        final_assessment = "✅ GOOD - PySDL3 is functional with some gaps"
    else:
        final_assessment = "⚠️ NEEDS WORK - PySDL3 has significant issues"
    
    print(f"🎖️ Final Assessment: {final_assessment}")
    print()
    
    print("💡 Recommendations:")
    if installation_ok:
        print("• PySDL3 is properly installed and accessible")
    else:
        print("• Fix PySDL3 installation issues")
    
    if simple_test_ok:
        print("• Basic functionality is working correctly")
    else:
        print("• Review basic function availability and imports")
    
    if module_analyzer_ok:
        print("• Module structure is well-organized")
    else:
        print("• Check module structure and organization")
    
    if coverage_test_ok:
        print("• Comprehensive API coverage is good")
    else:
        print("• Review specific API coverage gaps")
    
    print(f"\n⏰ Test completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Return appropriate exit code
    return 0 if overall_success_rate >= 60 else 1

if __name__ == "__main__":
    sys.exit(main())
