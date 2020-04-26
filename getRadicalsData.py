import json, re, csv, urllib, os
import urllib.request
from sys import platform

if platform == "darwin":
    import certifi
import pinyin

def getRadicalsData(): 

    fields = ["string", "altMandarin", "altDefinition"]
    url_radicals = f"http://ccdb.hemiola.com/characters/radicals?fields={','.join(fields)}"

    if platform == "darwin":
        json_file_radicals = urllib.request.urlopen(url_radicals, cafile=certifi.where()).read()
    else:
        json_file_radicals = urllib.request.urlopen(url_radicals).read()

    radicals = json.loads(json_file_radicals)
    entries = []

    for i in range(1,215):
        same_radicals = list(filter(lambda r: int(r["radical"]) == i, radicals))
        entry = same_radicals.pop(0)
        entry["alternativs"] = ", ".join([r["string"] for r in same_radicals])
        tone_number = re.search(r"\d", entry["altMandarin"]).group(0)
        entry["MandarinStyled"] = f"<div class=tone{tone_number}>{pinyin.get(entry['string'])}</div>"
        entries.append(entry)


    char_with_img = [c[0] for c in os.listdir("./media/img")]

    with open('./data/source.csv', 'w', newline='', encoding="UTF8") as csvfile:
        writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for d in entries:
            sound = f'[sound:cmn-{d["altMandarin"]}.mp3]'
            if d['string'] in char_with_img:
                ancient_img = f"<img src=\"{d['string']}_img_ancient.svg\">"
            else:
                ancient_img = ""
            writer.writerow([d["string"], d["MandarinStyled"], d["altMandarin"], d["altDefinition"], d["radical"], d["alternativs"], sound, ancient_img])

if __name__ == "__main__":
    getRadicalsData()