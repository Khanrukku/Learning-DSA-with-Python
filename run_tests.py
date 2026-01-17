"""
Test Runner Script

Run all tests with: python run_tests.py
"""

import subprocess
import sys

def run_tests():
    """Run all unit tests"""
    print("=" * 60)
    print("Running Data Structures & Algorithms Test Suite")
    print("=" * 60)
    
    try:
        # Run pytest
        result = subprocess.run(
            ['pytest', 'tests/', '-v', '--tb=short'],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✅ All tests passed!")
        else:
            print("\n❌ Some tests failed")
            sys.exit(1)
            
    except FileNotFoundError:
        print("pytest not found. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pytest'])
        run_tests()

if __name__ == "__main__":
    run_tests()
