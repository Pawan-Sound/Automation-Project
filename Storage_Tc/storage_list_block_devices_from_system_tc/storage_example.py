# storage_example.py
import json
from utils import run_cmd

def list_block_devices():
    rc, out, err = run_cmd("lsblk -o NAME,SIZE,TYPE,MOUNTPOINT -J")
    if rc != 0:
        raise RuntimeError(f"lsblk failed: {err}")
    data = json.loads(out)
    devices = []
    def walk(nodes):
        for n in nodes:
            name = n.get("name")
            size = n.get("size")
            typ  = n.get("type")
            mount = n.get("mountpoint")
            devices.append({"name": name, "size": size, "type": typ, "mountpoint": mount})
            if "children" in n:
                walk(n["children"])
    walk(data.get("blockdevices", []))
    return devices

if __name__ == "__main__":
    for d in list_block_devices():
        print(d)
