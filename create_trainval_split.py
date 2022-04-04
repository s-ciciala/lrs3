import os
import sys
import shutil
##SPLIT 80:10:10
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


def unique_check():
    print("VAL LIST LEN: ",len(VAL_LIST) ," SHOULD BE :",VAL_SIZE )
    print("TRAIN LIST LEN: ",len(TRAIN_LIST) ," SHOULD BE :",TOTAL_SPLIT - VAL_SIZE )
    for i in TRAIN_LIST:
        for j in VAL_LIST:
            if i == j:
                print("SPLIT WRONG ", str(i))
                break
    print("ALL GOOD ")

unique_check()

##MAKE VAL SET##
if not os.path.exists(PATH_TO_LRS3_VAL):
    os.mkdir(PATH_TO_LRS3_VAL)

for val_dir in VAL_LIST:
    make_folders = os.path.join(PATH_TO_LRS3_VAL,val_dir)
    root_folder = os.path.join(PATH_TO_LRS3_TRAINVAL,val_dir)
    if not os.path.exists(make_folders):
        os.mkdir(make_folders)
    val_examples_list = os.listdir(root_folder)
    for val_example_file in val_examples_list:
        file = os.path.join(root_folder,val_example_file)
        copy = os.path.join(make_folders,val_example_file)
        if not os.path.exists(copy):
            copied_file =  shutil.copy(file,copy)
            print("COPIED OVER :",copied_file)

##MAKE TRAIN SET##
if not os.path.exists(PATH_TO_LRS3_TRAIN):
    os.mkdir(PATH_TO_LRS3_TRAIN)

for train_dir in TRAIN_LIST:
    make_folders = os.path.join(PATH_TO_LRS3_TRAIN,train_dir)
    if not os.path.exists(make_folders):
        os.mkdir(make_folders)
    #shutil.copytree(os.path.join(PATH_TO_LRS3_TRAINVAL, train_dir), PATH_TO_LRS3_TRAIN)

for train_dir in TRAIN_LIST:
    make_folders = os.path.join(PATH_TO_LRS3_TRAIN,train_dir)
    root_folder = os.path.join(PATH_TO_LRS3_TRAINVAL,train_dir)
    if not os.path.exists(make_folders):
        os.mkdir(make_folders)
    train_examples_list = os.listdir(root_folder)
    for train_example_file in train_examples_list:
        file = os.path.join(root_folder,train_example_file)
        copy = os.path.join(make_folders,train_example_file)
        if not os.path.exists(copy):
            copied_file =  shutil.copy(file,copy)
            print("COPIED OVER :",copied_file)





