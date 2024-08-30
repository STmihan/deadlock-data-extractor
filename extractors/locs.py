from pathlib import Path
import shutil

from config import DEADLOCK_PATH, PATH_TO_GC, PATH_TO_HEROES


def dump_localization():
    shutil.copy(Path(DEADLOCK_PATH) / PATH_TO_GC,     "data/citadel_gc_english.txt")
    shutil.copy(Path(DEADLOCK_PATH) / PATH_TO_HEROES, "data/citadel_heroes_english.txt")
