import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from IPython.display import Audio
import moviepy.editor as mp
import librosa
import os
import sys
from pydub import AudioSegment
import tqdm as tqdm

SPLITS = ["test/","train/","val/"]
PATH_TO_LRS3 = "/disk/scratch2/s1834237/LRS3_wav/LRS3/"

def convert_mp4(mp4_path, output_file):
    '''
    reads the mp4 file and wrties to desired format
    :param mp4_path (string): needs to be in form -r"Shrek.mp4"- as r indicates read
    :param output_file (string): needs to be in form -r"Shrek.wav"- as r indicates read
    :return None: writes file
    '''
    video = mp.VideoFileClip(mp4_path)  # here sample.mp4 is the name of video clip. 'r' indicates that we are
    video.audio.write_audiofile(output_file)  # Here output_file is the name of the audio file with type e.g "Shrek.wav"

    return video.audio.to_soundarray()

for split in SPLITS:
    dataset_path = PATH_TO_LRS3 + split
    files = os.listdir(dataset_path)
    print("SPLIT ", str(split))
    for file in tqdm(range(len(files))):
        file_path = dataset_path + files[file] +"/"
        examples = os.listdir(file_path)
        for example in examples:
            if ".mp4" in example:
                mp4_path = file_path + example
                wav_form = example.split(".")
                audio_file = wav_form[0] + ".wav"
                wav_path = file_path + audio_file
                convert_mp4(mp4_path,wav_path)

