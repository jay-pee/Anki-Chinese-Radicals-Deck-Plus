import csv
import os
import urllib.request


def download_ancient_img():
    with open("./data/ancient_img_url.csv", "r", encoding="UTF8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        img_list = os.listdir("./media")
        downloaded_img = [i[0] for i in img_list]
        for row in reader:
            if row[0] not in downloaded_img:
                try:
                    urllib.request.urlretrieve(
                        row[1], f"./media/{row[0]}_img_ancient.svg"
                    )
                except:
                    print(f"can't load IMG {row[0]}")


if __name__ == "__main__":
    download_ancient_img()
