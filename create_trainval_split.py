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
PATH_TO_LRS3_TEST = "/disk/scratch2/s1834237/LRS3/test"
METADATA_DIR = "/disk/scratch2/s1834237/espnet/egs/lrs3/asr1/data/METADATA"

Filelist_test = "Filelist_test"
Filelist_train = "Filelist_test"
Filelist_val = "Filelist_test"
fileLists = ["test","train","val"]

sub_dirs = os.listdir(PATH_TO_LRS3_TRAINVAL)
assert len(sub_dirs) == TOTAL_SPLIT
VAL_LIST = sub_dirs[:VAL_SIZE]
TRAIN_LIST = sub_dirs[VAL_SIZE:TOTAL_SPLIT]

def stringify (num):
    if num < 10:
        return "000"+str(num)
    else:
        return "00"+str(num)

def make_metadata(file_lists):
    for split in fileLists:
        filtered = []
        if split == "test":
            root_path = PATH_TO_LRS3_TEST
        elif split == "train":
            root_path = PATH_TO_LRS3_TRAIN
        else:
            root_path = PATH_TO_LRS3_VAL
        sub_dir = os.listdir(root_path)
        for example in sub_dir:
            example_path = os.path.join(root_path, example)
            all_mp4s = os.listdir(example_path)
            as_numbers = []
            ##We do this in order
            for mp4 in all_mp4s:
                if ".mp4" in mp4:
                    as_numbers.append(int(mp4.split('.')[0]))
            as_numbers.sort()
            for value in as_numbers:
                target_string = example + "/" + stringify(value)
                filtered.append(target_string)
            #print(filtered)
            ##WIRTE TO FILE##
            filename = METADATA_DIR + "/Filelist_"+split
            file = open(filename, "w")
            final_line = filtered[-1]
            for line in filtered:
                if line != final_line:
                    file.writelines(line+"\n")
                else:
                    file.writelines(line)
        print("DONE WRITING ",split)
        file.close()


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

make_metadata(fileLists)



