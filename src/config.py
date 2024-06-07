from pathlib import Path
import src.utils as utils

ROOT_DIR = Path(__file__).parent.parent
OUT_DIR = ROOT_DIR / 'out'
FIGURES_DIR = OUT_DIR / 'figures'

for dir in (OUT_DIR, FIGURES_DIR):
    utils.ensure_dir_exists(dir)