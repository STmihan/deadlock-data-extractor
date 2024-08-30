import shutil

FROM_PATH = "deadlockery/deadlock-other-data/stringmap.json"
TO_PATH = "data/stringmap.json"

def dump_stringmap():
    # TODO: Just copy old one from deadlockery for now
    # Later I will implement a proper stringmap extractor

    if shutil.os.path.exists(TO_PATH):
        shutil.os.remove(TO_PATH)
    shutil.copyfile(FROM_PATH, TO_PATH)
