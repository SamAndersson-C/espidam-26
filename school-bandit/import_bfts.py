from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent
BFTS_DIR = ROOT_DIR / "bfts"

if str(BFTS_DIR) not in sys.path:
    sys.path.insert(0, str(BFTS_DIR))
