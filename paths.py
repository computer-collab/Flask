import os

from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
CURRENT_DIR = CURRENT_FILE.parent


class CONSTANTS:
    ROOT = Path(__file__).resolve().parent

__NAME__ = __name__

print(CURRENT_FILE)
print(CONSTANTS.ROOT)
