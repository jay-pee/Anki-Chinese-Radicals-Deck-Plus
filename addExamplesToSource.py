import csv

from hanzipy_decomposer import HanziDecomposer


def add_examples_to_source():
    inst = HanziDecomposer()
    # Read radicals from a CSV file
    with open("./data/source.csv", mode="r", encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter="\t")
        data = [row for row in reader]

    # Process each radical
    radical_characters = []
    for row in data:
        try:
            characters = inst.get_characters_with_component(row[0])
            # Limit to first 5 characters
            if characters is not None:
                characters = characters[:5] if len(characters) > 5 else characters
                radical_characters.append(", ".join(characters))
            else:
                raise KeyError
        except KeyError:
            radical_characters.append("")

    # Write the updated data to a new CSV file
    with open(
        "./data/source_examples.csv", mode="w", encoding="UTF-8", newline=""
    ) as file:
        combined_data = [
            row + [rad_chars] for row, rad_chars in zip(data, radical_characters)
        ]
        writer = csv.writer(
            file, delimiter="\t", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        writer.writerows(combined_data)

        print("Finished!")


if __name__ == "__main__":
    add_examples_to_source()
