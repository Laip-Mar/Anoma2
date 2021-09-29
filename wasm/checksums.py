import json
import glob
import hashlib
import os

checksums = {}
for wasm in sorted(glob.glob("wasm/*.wasm")):
    basename = os.path.basename(wasm)
    file_name = os.path.splitext(basename)[0] if wasm.count(".") == 1 else os.path.splitext(basename)[0].split('.')[0]
    checksums["{}.wasm".format(file_name)] = "{}.{}.wasm".format(file_name, hashlib.sha256(open(wasm, "rb").read()).hexdigest())
    os.rename(wasm, checksums["{}.wasm".format(file_name)])

json.dump(checksums, open("wasm/checksums.json", "w"))