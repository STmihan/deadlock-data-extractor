import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import List, TypedDict

from config import DEADLOCK_PATH, DECOMPILER

ITEMS_PATH = "panorama/images/upgrades"
LOC_PATH = "data/citadel_heroes_english.txt"

def dump_items():
    subprocess.run([
        DECOMPILER,
        "-i",
        Path(DEADLOCK_PATH) / "pak01_dir.vpk",
        "--output",
        "data/vtex_c/",
        "--vpk_filepath",
        ITEMS_PATH
    ])

    files = Path("data/vtex_c/").rglob("*.vtex_c")
    for file in files:
        print(file)
        old_path = file.__str__()
        old_path = old_path.replace("\\", "/")
        new_path = old_path.replace("vtex_c/panorama/images/upgrades/", "items/")
        new_path = new_path.replace(".vtex_c", ".png")
        subprocess.run([
            DECOMPILER,
            "-i",
            old_path,
            "-o",
            new_path
        ])
        os.rename(new_path, new_path.replace("_psd", ""))
    
    shutil.rmtree("data/vtex_c")
