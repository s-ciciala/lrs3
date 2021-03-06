import multiprocessing as mp
import os
import sys

print("make_files")

def main(sourcedir, filelistdir, savedir, dset, nj):
    """Prepare the Kaldi files.

    Args:
        sourcedir (str): LRS3 dataset dir.
        filelist (str): The dir of the mp4 file, it should be like
                        '5535415699068794046/00001'
        savedir (str): The dir save the Kaldi files.
        dset (str): Which set. For this code dset is pretrain set.
        nj (str): Number of multi processes.

    """
    nj = int(nj)
    if nj > 1:
        multicore = True
    else:
        multicore = False
    ##MUST LOWERCASE
    dset = dset.lower()
    filelistdir = filelistdir + "/" + "Filelist_" + dset
    print("HERE")
    print(filelistdir)
    with open(filelistdir) as filelists:
        filelist = filelists.readlines()
    for i in range(len(filelist)):
        filelist[i] = filelist[i].strip("\n")
    if multicore is True:
        print("VATT")
        print(dset)
        print(savedir)
        print(sourcedir)
        pool = mp.Pool(nj)
        sourcedir += "/" + dset
        print(sourcedir)
        print(len(filelist))
        job_args = [(i, dset, savedir, sourcedir) for i in filelist]
        print("JOBED")
        pool.map(product_helper, job_args)
    else:
        for i in filelist:
            set(i, dset, savedir, sourcedir)

def set(info, s, savedir, sourcedir):
    """Make the Kaldi files.

    Args:
        info (str): The file name.
        s (str): Which set. For this code dset is pretrain set.
        savedir (str): The dir save the Kaldi files.
        sourcedir (str): LRS3 dataset dir.

    """
    print("SET")
    textdir = savedir + "/text"
    utt2spkdir = savedir + "/utt2spk"
    wavdir = savedir + "/wav.scp"
    print(textdir)
    print(utt2spkdir)
    print(wavdir)

    info = info.split()
    info[0] = info[0].split("/")
    info[0] = "LRS3_" + info[0][0] + "_" + info[0][1] + "m"
    name = info[0]
    name = name.split("_")
    f = os.path.join(name[1], name[2][:-1])

    textfile = os.path.join(sourcedir, f + ".txt")
    mp4dir = os.path.join(sourcedir, f + ".mp4")
    with open(textfile) as filelists:
        text = filelists.readlines()
    text = text[0].split(":")[1]
    splitname = f.split("/")
    title = "LRS3_" + splitname[0] + "_" + splitname[1] + "m"
    with open(textdir, "a") as textprocess:
        textprocess.writelines(title + "" + text)
        textprocess.close()

    with open(utt2spkdir, "a") as utt:
        utt.writelines(title + " LRS3_" + splitname[0] + "_" + splitname[1] + "m\n")
        utt.close()

    command1 = "ffmpeg -y -i"
    command2 = "-vn -ac 2 -ar 16000 -ab 320k -f wav /tmp/tmp.$$; cat /tmp/tmp.$$ |\n"
    wavscp = " ".join([title, command1, mp4dir, command2])
    with open(wavdir, "a") as wav:
        wav.writelines(wavscp)
        wav.close()

def product_helper(args):
    return set(*args)
# hand over parameter overview
# sys.argv[1] = sourcedir (str): The LRS2 dataset dir
#                                (e.g. /LRS2/data/lrs2_v1/mvlrs_v1/main)
# sys.argv[2] = filelistdir (str): The directory containing the dataset
#                                 Filelists (METADATA)
# sys.argv[3] = savedir (str): Save directory, datadir of the clean audio dataset
# sys.argv[4] = dset (str): Which set. There are pretrain, Train, Val, Test set.
# sys.argv[5] = nj (str): Number of multi processes.


print("agrs")
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])

main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
