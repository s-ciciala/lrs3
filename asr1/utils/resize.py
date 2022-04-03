import os

utt2spk_path = "/home/szy/Documents/code/espnet/egs/tedlium3/asr1/data/train/utt2spk"
feats_path = "/home/szy/Documents/code/espnet/egs/tedlium3/asr1/data/train/utt2dur"
feats_lines = list()
utts_lines = list()

with open(feats_path) as file:
    for line in file:
        feats_lines.append(line)

with open(utt2spk_path) as file:
    for line in file:
        utts_lines.append(line)


def create_dictionary(feats_lines,utts_lines):
    our_dict_feats = {}
    our_dict_utts = {}
    ###Initialize##
    counter = 0
    for i in feats_lines:
        k = i.split("_")
        if k[0] not in our_dict_feats.keys():
            our_dict_feats[k[0]] = 0
    for i in utts_lines:
        k = i.split("_")
        if k[0] not in our_dict_utts.keys():
            our_dict_utts[k[0]] = 0
    ###############
    for i in feats_lines:
        k = i.split("_")
        our_dict_feats[k[0]] += 1
    for i in utts_lines:
        k = i.split("_")
        our_dict_utts[k[0]] += 1
    return our_dict_utts, our_dict_feats


def check_same_keys(utts_dict, feats_dict):
    utts_keys =  utts_dict.keys()
    feats_keys = feats_dict.keys()
    if(len(utts_dict) == len(feats_dict) and utts_keys == feats_keys):
        return True
    else:
        return False

def check_counts(utts_dict,feats_dict):
    keys = utts_dict.keys()
    wrong_counts = list()
    for key in keys:
        #print(utts_dict[key], feats_dict[key])
        if utts_dict[key] != feats_dict[key]:
            wrong_counts.append(key)
    return wrong_counts


def change_lists(feats_lines,utts_lines,wrong_counts):
    shorter = ""
    correct_feat_lines = list()
    correct_utts_lines = list()
    if(len(wrong_counts) == 0):
        exit()

    elif (len(feats_lines) < len(utts_lines)):
        shorter ="feats"
        longer ="utts"
    else:
        shorter ="utts"
        longer = "feats"
    print(shorter)
    for wrong in wrong_counts:
        if (shorter == "utts"):
            correct_num = 0
            for i in utts_lines:
                k = i.split("_")
                if k[0] == wrong:
                    correct_num +=1
            print(correct_num)

            for feat in feats_lines:
                check = feat.split("_")
                if check[0] != wrong:
                    correct_feat_lines.append(feat)
                else:
                    if(correct_num != 0):
                        correct_num -= 1
                        correct_feat_lines.append(feat)
            return correct_feat_lines,longer
        else:
            correct_num = 0
            for i in feats_lines:
                k = i.split("_")
                if k[0] == wrong:
                    correct_num +=1
            print(correct_num)

            for utt in utts_lines:
                check = utt.split("_")
                if check[0] != wrong:
                    correct_utts_lines.append(utt)
                else:
                    if(correct_num != 0):
                        correct_num -= 1
                        correct_utts_lines.append(utt)
            print("changed was " + longer)
            return correct_utts_lines,longer

def write_new_files(feats_path,utt2spk_path,utts_lines,feats_lines):
    ##check len
    print(len(utts_lines))
    print(len(feats_lines))
    if(len(utts_lines)==len(feats_lines)):
        print("all good")
    utts_file = open(utt2spk_path, "w")
    #feats_file = open(feats_path, "w")
    for line in range(len(utts_lines)):
        utts_file.write(utts_lines[line])
        #feats_file.write(feats_lines[line])

utts_dict, feats_dict = create_dictionary(feats_lines,utts_lines)
check_same_keys(utts_dict,feats_dict)
wrong_counts = check_counts(utts_dict,feats_dict)
print(len(wrong_counts))
if(len(wrong_counts) == 0):
    exit()
    print("Exit")
fixed,verdict = change_lists(feats_lines,utts_lines,wrong_counts)
print(len(utts_lines))
print(len(feats_lines))
print(len(fixed))
print(verdict)
print("            ")
if (verdict == "utts"):
    utts_lines = fixed
else:
    feats_lines = fixed
print(len(utts_lines))
print(len(feats_lines))
print(len(fixed))

write_new_files(feats_path,utt2spk_path,utts_lines,feats_lines)
