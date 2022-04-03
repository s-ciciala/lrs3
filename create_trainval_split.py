import os
import sys

TOTAL_SPLIT = 4004
TEST_SIZE = 412
VAL_SIZE = 412
PATH_TO_LRS3_TRAINVAL = "/disk/scratch2/s1834237/LRS3/trainval"
PATH_TO_LRS3_TRAIN = "/disk/scratch2/s1834237/LRS3/train"
PATH_TO_LRS3_VAL = "/disk/scratch2/s1834237/LRS3/val"

sub_dirs = os.listdir(PATH_TO_LRS3_TRAINVAL)
assert len(sub_dirs) == TOTAL_SPLIT
VAL_LIST = sub_dirs[:VAL_SIZE]
TRAIN_LIST = sub_dirs[VAL_SIZE:TOTAL_SPLIT]

##MAKE VAL SET##
if not os.path.exists(PATH_TO_LRS3_VAL):
    os.mkdir(PATH_TO_LRS3_VAL)

for val_dir in VAL_LIST:
    print(val_dir)


##MAKE TRAIN SET##
if not os.path.exists(PATH_TO_LRS3_TRAIN):
    os.mkdir(PATH_TO_LRS3_TRAIN)






