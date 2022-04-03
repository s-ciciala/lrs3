import json

path_to_json = "/home/szy/Documents/code/espnet/egs/LRS3/asr1/dump/val/deltafalse/data_unigram500.json"

with open(path_to_json, "rb") as f:
    print(f)
    ld = json.load(f)
    load = ld["utts"]
    print("HERE")
    print(ld)
    print("PAST")