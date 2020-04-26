import csv, re, os
from shutil import copyfile


path_syllabs = "./syllabs/" 
syllabs_list = os.listdir(path_syllabs)

with open('./data/source.csv', 'r', newline='', encoding="UTF8") as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for line in reader:
        for s in syllabs_list:
            if line[2] in s:
                copyfile(path_syllabs+s, './media/audio/'+s)