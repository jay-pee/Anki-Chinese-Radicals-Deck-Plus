import copy
import csv
import os

import genanki


def generate_deck():
    result_dict = []

    with open("./data/source_examples.csv", encoding="UTF8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            template_dict = dict.fromkeys(
                [
                    "Hanzi",
                    "Pinyin",
                    "Pinyin RAW",
                    "English",
                    "Kanxi Number",
                    "Alternatives",
                    "Sound",
                    "Ancient Character",
                    "Examples",
                ]
            )
            for i, key in enumerate(template_dict.keys()):
                template_dict[key] = row[i]
            result_dict.append(template_dict)

    print(result_dict[0])

    my_model = genanki.Model(
        1087741751,
        "Chinese (Radicals)",
        fields=[
            {"name": "Hanzi"},
            {"name": "Pinyin"},
            {"name": "English"},
            {"name": "Kanxi Number"},
            {"name": "Alternatives"},
            {"name": "Sound"},
            {"name": "Ancient Character"},
            {"name": "Examples"},
        ],
        templates=[
            {
                "name": "Recall",
                "qfmt": "\n".join(
                    [
                        "<div class=container>",
                        "<div class=radical_number>Radical Number: {{Kanxi Number}}</div>",
                        "<div class=tags>{{Deck}} {{#Tags}} -- {{/Tags}}{{Tags}}</div>",
                        "</div>",
                        "<div class=chinese> {{Hanzi}}</div>",
                        "{{#Alternatives}}<div class=note>Alternatives:  <div class=chinese>{{Alternatives}}</div></div>{{/Alternatives}}",
                    ]
                ),
                "afmt": "\n".join(
                    [
                        "{{FrontSide}}",
                        "<hr>",
                        "<div>{{English}}</div>",
                        "<br>",
                        "<div class=reading>{{Pinyin}}</div>",
                        "<div class=note>Examples:{{Examples}}</div>",
                        "{{#Ancient Character}}<div class=note>Ancient Character:</div>{{Ancient Character}}{{/Ancient Character}}",
                        "<br>",
                        "{{Sound}}",
                    ]
                ),
            },
        ],
        css="\n".join(
            [
                ".card {",
                "font-family: arial;",
                "font-size: 20px;",
                "text-align: center;",
                "color: black;",
                "background-color: white;",
                "word-wrap: break-word;",
                "}",
                "img {",
                "border: 1px solid #ddd;",
                "border-radius: 4px;",
                "padding: 5px;",
                "width: 150px;",
                "}",
                '.win .chinese { font-family: "MS Mincho", "ＭＳ 明朝"; }',
                ".mac .chinese { }",
                '.linux .chinese { font-family: "Kochi Mincho", "東風明朝"; }',
                '.mobile .chinese { font-family: "Hiragino Mincho ProN"; }',
                ".chinese { font-size: 30px;}",
                ".reading { font-size: 20px;}",
                ".comment {font-size: 15px; color:grey;}",
                ".tags {color:gray;text-align:right;font-size:10pt;}",
                ".radical_number {color:gray;text-align:left;font-size:10pt;}",
                ".note {color:gray;font-size:12pt;margin-top:20pt;}",
                ".hint {font-size:12pt;}",
                "",
                ".tone1 {color: red;}",
                ".tone2 {color: orange;}",
                ".tone3 {color: green;}",
                ".tone4 {color: blue;}",
                ".tone5 {color: gray;}",
                "",
                ".container {",
                "  display: grid;",
                "  grid-gap: 1rem;",
                "  grid-template-columns:  grid-template-columns: repeat(2, 1fr);",
                '  grid-template-areas:"a b"',
                "}",
            ]
        ),
    )

    my_deck = genanki.Deck(1540858611, "Chinese Radicals Deck+")
    for item in result_dict:
        my_note = genanki.Note(
            model=my_model,
            fields=[
                item["Hanzi"],
                item["Pinyin"],
                item["English"],
                item["Kanxi Number"],
                item["Alternatives"],
                item["Sound"],
                item["Ancient Character"],
                item["Examples"],
            ],
        )
        my_deck.add_note(copy.deepcopy(my_note))
    my_package = genanki.Package(my_deck)
    media_img_files = ["./media/img/" + i for i in os.listdir("./media/img")]
    media_audio_files = ["./media/audio/" + i for i in os.listdir("./media/audio")]
    my_package.media_files = media_img_files + media_audio_files
    my_package.write_to_file("./decks/Chinese-Radicals-Deck-Plus.apkg")


if __name__ == "__main__":
    generate_deck()
