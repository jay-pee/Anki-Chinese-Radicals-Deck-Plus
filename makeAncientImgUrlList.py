from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import re
import csv
from socket import timeout
import logging

def makeAncientImgUrlList():
    character_list = []
    with open("source.csv", "r", encoding="UTF8") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        url_list = []
        for row in reader:
            character = row[0]
            char_decoded = urllib.parse.quote(character)
            url = f"http://www.zdic.net/hans/{char_decoded}"
            url_list.append(url)
            character_list.append(character)

    url_img_list = []
    character_list_copy = []
    while url_list:
        url = url_list.pop(0)
        char = character_list.pop(0)
        try:
            page = urllib.request.urlopen(url, timeout=10).read()
        except timeout:
            logging.error('socket timed out - URL %s', url)
            url_list.append(url)
            character_list.append(char)
            continue
        else:
            logging.info('Access successful.')

        soup = BeautifulSoup(page, 'html.parser')
        img = soup.find(attrs={"class": "lazy ypic"})
        if not img:
            logging.error('No Image - URL %s', url)
            character_list_copy.append(char)
            url_img_list.append("")
            continue

        url_img = re.sub(r'//','http://',img.attrs["data-original"])
        url_img_list.append(url_img)
        character_list_copy.append(char)

    with open("ancient_img_url.csv", "w", encoding="UTF8") as csvfile:
        writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for char, url in zip(character_list_copy , url_img_list):
            writer.writerow([char, url])

if __name__ == "__main__":
    makeAncientImgUrlList()