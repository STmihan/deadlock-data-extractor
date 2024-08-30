import os
from pathlib import Path
import shutil
import subprocess

from config import DEADLOCK_PATH, DECOMPILER

HEROES_PATH = "panorama/images/heroes"

def dump_heroes():
    subprocess.run(
    [
        DECOMPILER,
        "-i",
        Path(DEADLOCK_PATH) / "pak01_dir.vpk",
        "--output",
        "data/vtex_c/",
        "--vpk_filepath",
        HEROES_PATH,
    ]
    )
    shutil.rmtree(f"data/vtex_c/{HEROES_PATH}/guns")
    files = os.listdir(f"data/vtex_c/{HEROES_PATH}")
    for file in files:
        if "_card_" in file:
            continue
        else:
            os.remove(f"data/vtex_c/{HEROES_PATH}/{file}")
    
    files = os.listdir(f"data/vtex_c/{HEROES_PATH}")
    for file in files:
        new_name = file.replace("_psd", "")
        new_name = new_name.replace("_card", "")
        new_name = new_name.replace(".vtex_c", ".png")
        subprocess.run(
            [
                DECOMPILER,
                "-i",
                f"data/vtex_c/{HEROES_PATH}/{file}",
                "-o",
                f"data/heroes/{file}",
            ]
        )
        os.rename(f"data/heroes/{file.replace(".vtex_c", ".png")}", f"data/heroes/{new_name}")
    
    shutil.rmtree(f"data/vtex_c")
    
