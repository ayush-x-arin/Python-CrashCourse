"""
Interactive Assignment Test Runner
==================================
Usage:
  python3 test_runner.py 1      # Run tests for Lesson 01
  python3 test_runner.py 2      # Run tests for Lesson 02
  python3 test_runner.py all    # Run all available tests
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LESSON_TEST_MAP = {
    "1": "tests/test_01_lists.py",
    "01": "tests/test_01_lists.py",
    "2": "tests/test_02_dicts.py",
    "02": "tests/test_02_dicts.py",
    "3": "tests/test_03_stacks.py",
    "03": "tests/test_03_stacks.py",
    "4": "tests/test_04_universal_backend.py",
    "04": "tests/test_04_universal_backend.py",
}


def run_lesson_test(lesson_key: str):
    if lesson_key in ["all", "run-all"]:
        suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test_*.py")
    else:
        test_file = LESSON_TEST_MAP.get(lesson_key)
        if not test_file:
            print(f"❌ Unknown lesson number '{lesson_key}'. Available: {list(LESSON_TEST_MAP.keys())}")
            sys.exit(1)
        suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern=Path(test_file).name)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! Fantastic work! 🚀")
        sys.exit(0)
    else:
        print(f"\n❌ {len(result.failures) + len(result.errors)} test(s) failed. Check tracebacks above and try again!")
        sys.exit(1)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "1"
    run_lesson_test(target)
