#!/usr/bin/env python3

import os
import json

# Things that this script checks
# 
# * make sure mrinfo runs successfully on specified t1 file
# * make sure t1 is 3d
# * raise warning if t1 transformation matrix isn't unit matrix (identity matrix)

# display where this is running
# import socket
# print(socket.gethostname())

with open('config.json', encoding='utf8') as config_json:
    config = json.load(config_json)

results = {"errors": [], "warnings": []}

if not os.path.exists("secondary"):
    os.mkdir("secondary")

if not os.path.exists("output"):
    os.mkdir("output")

files=[
    ["os_raw", "OS_Raw.csv"], 
    ["os_centroid", "OScentroid.csv"], 
    ["od_raw", "OD_Raw_csv"], 
    ["od_centroid", "ODcentroid.csv"],
]

for file in files:
    id=file[0]
    name=file[1]
    if not os.path.exists(config[id]):
        results["errors"].append(id+" not found")
        continue
        
    if os.path.lexists("output/"+name):
        os.remove("output/"+name)
    os.symlink("../"+config[id], "output/"+name)

with open("product.json", "w") as fp:
    json.dump(results, fp)

if len(results["errors"]) > 0:
    print(results["errors"])

print("done");
