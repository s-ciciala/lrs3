SPLITS = ["test/","train/","val/"]
PATH_TO_DUMP = "/disk/scratch2/s1834237/espnet/egs/lrs3/dump/"
DELTA = "deltafalse/"
FILE = "data_unigram500.json"

fileLists = ["test","train","val"]


for split in SPLITS:
    curr_set = PATH_TO_DUMP + split
    curr_delt = curr_set + DELTA
    file = curr_delt + FILE
    with open(file) as f:
        lines = f.readlines()
        if len(lines[0]) > 5:
            print("Was: ",lines[0])
            lines[0] = "{\n"
            print("Is: ",lines[0])
            with open(file, "w") as k:
                k.writelines(lines)
        else:
            print("NO NEED TO FIX")
