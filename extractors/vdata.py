import os
import shutil
import subprocess

def dump_vdata():
    if not os.path.exists("data/vdata"):
        os.mkdir("data/vdata")
    else:
        shutil.rmtree("data/vdata")
        os.mkdir("data/vdata")
    subprocess.run([
        "dotnet",
        "run",
        "--project",
        "../../deadlockery/kv3bs/kv3bs.csproj"
    ], cwd="data/vdata")