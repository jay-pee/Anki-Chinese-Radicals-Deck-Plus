from makeAncientImgUrlList import *
from downloadAncientImg import *
from generateDeck import *
from getRadicalsData import *

import os

MAKE_NEW_ANCIENT_IMG_LIST = False
REDOWNLOAD_ANCIENT_IMG = False

if __name__ == "__main__":
    if MAKE_NEW_ANCIENT_IMG_LIST:
        makeAncientImgUrlList()
    if REDOWNLOAD_ANCIENT_IMG:
        downloadAncientImg()
    getRadicalsData()
    overwriteRadicalData()
    os.system("node addExamplesToSource.js") #todo: replace this by python script
    generateDeck()
