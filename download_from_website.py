import csv
import os
import urllib.request

img_list = os.listdir("./media")
downloaded_img = [i[0] for i in img_list]


def download_from_website(url, name, appendix):
    if url not in downloaded_img:
        try:
            urllib.request.urlretrieve(
                url, f"./media/stroke_order/{name}_{appendix}.svg"
            )
        except Exception as e:
            print(f"can't load IMG {url}")
            print(e)


if __name__ == "__main__":
    url_base = (
        "https://raw.githubusercontent.com/skishore/makemeahanzi/master/svgs-still"
    )
    with open("./data/source.csv", "r", encoding="UTF8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            char_int = ord(row[0])
            download_from_website(
                f"{url_base}/{char_int}-still.svg", row[0], "stroke_order"
            )
