import shutil
import os
import time

from extractors.abilities import dump_abilities
from extractors.heroes import dump_heroes
from extractors.heroes_json import create_heroes_json
from extractors.items_json import create_items_json
from extractors.locs import dump_localization
from extractors.stringmap import dump_stringmap
from extractors.vdata import dump_vdata
from extractors.items import dump_items

if not os.path.exists("data"):
    os.mkdir("data")
else:
    shutil.rmtree("data")
    os.mkdir("data")

start_time = time.time()

dump_localization()
dump_vdata()
dump_stringmap()
dump_heroes()
dump_abilities()
create_heroes_json()
dump_items()
create_items_json()

print(f"Extraction took {time.time() - start_time} seconds")
