import csv
import os
from shutil import copyfile

path_syllabs = "./syllabs/"
syllabs_list = os.listdir(path_syllabs)


def copy_audio_from_cmn():
    with open("./data/source.csv", "r", newline="", encoding="UTF8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for line in reader:
            for s in syllabs_list:
                if line[2] in s:
                    copyfile(path_syllabs + s, "./media/audio/" + s)


if __name__ == "__main__":
    copy_audio_from_cmn()
