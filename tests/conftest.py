# Ensure the project root is on sys.path so that `import agent` and `import tools` work
import os
import sys

# Calculate project root (parent of tests directory)
_TESTS_DIR = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.abspath(os.path.join(_TESTS_DIR, os.pardir))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)