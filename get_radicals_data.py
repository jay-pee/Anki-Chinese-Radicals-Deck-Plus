import csv
import os
import re

import requests


def __add_tone_mark(pinyin_with_number):
    tone_marks = {
        "a": ["ā", "á", "ǎ", "à", "a"],
        "e": ["ē", "é", "ě", "è", "e"],
        "i": ["ī", "í", "ǐ", "ì", "i"],
        "o": ["ō", "ó", "ǒ", "ò", "o"],
        "u": ["ū", "ú", "ǔ", "ù", "u"],
        "ü": ["ǖ", "ǘ", "ǚ", "ǜ", "ü"],
        "A": ["Ā", "Á", "Ǎ", "À", "A"],
        "E": ["Ē", "É", "Ě", "È", "E"],
        "I": ["Ī", "Í", "Ǐ", "Ì", "I"],
        "O": ["Ō", "Ó", "Ǒ", "Ò", "O"],
        "U": ["Ū", "Ú", "Ǔ", "Ù", "U"],
        "Ü": ["Ǖ", "Ǘ", "Ǚ", "Ǜ", "Ü"],
    }

    if pinyin_with_number[-1].isdigit():
        tone_number = int(pinyin_with_number[-1]) - 1
        pinyin_base = pinyin_with_number[:-1]

        for vowel in tone_marks:
            if vowel in pinyin_base:
                return pinyin_base.replace(vowel, tone_marks[vowel][tone_number])

    return pinyin_with_number  # return the original string if no tone number is found


def get_radicals_data():
    fields = ["string", "kMandarin", "altDefinition"]
    url_radicals = (
        f"http://ccdb.hemiola.com/characters/radicals?fields={','.join(fields)}"
    )

    # Sending GET request
    response = requests.get(url_radicals, headers={"User-Agent": "XY"})

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        radicals = response.json()
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        exit(1)

    entries = []

    for i in range(1, 215):
        same_radicals = filter(lambda r: int(r["radical"]) == i, radicals)
        entry = next(same_radicals)
        entry["alternativs"] = ", ".join([r["string"] for r in same_radicals])
        pinyin_iter = re.finditer(r"\w+\d", entry["kMandarin"])
        entry["MandarinStyled"] = ""
        for pinyin in pinyin_iter:
            tone_number = re.search(r"\d", pinyin.group(0)).group(0)
            entry[
                "MandarinStyled"
            ] += f"<div class=tone{tone_number}>{__add_tone_mark(pinyin.group().lower())}</div>, "
        entry["MandarinStyled"] = entry["MandarinStyled"][:-2]
        entries.append(entry)

    char_with_img = [c[0] for c in os.listdir("./media/img")]

    with open("./data/source.csv", "w", newline="", encoding="UTF8") as csvfile:
        writer = csv.writer(
            csvfile, delimiter="\t", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        for d in entries:
            first_pinyin = (
                re.search(r"^\w+\d", d["kMandarin"]).group(0).lower().replace("ü", "v")
            )
            sound = f"[sound:cmn-{first_pinyin}.mp3]"
            if d["string"] in char_with_img:
                ancient_img = f"<img src=\"{d['string']}_img_ancient.svg\">"
            else:
                ancient_img = ""

            stroke_order = f"<img src=\"{d['string']}_stroke_order.svg\">"
            writer.writerow(
                [
                    d["string"],
                    d["MandarinStyled"],
                    d["kMandarin"].lower(),
                    d["altDefinition"],
                    d["radical"],
                    d["alternativs"],
                    sound,
                    ancient_img,
                    stroke_order,
                ]
            )


if __name__ == "__main__":
    get_radicals_data()
