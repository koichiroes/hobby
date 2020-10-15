from os import write
from xml.etree import ElementTree
import sys
from pathlib import Path
import csv
import random

dir = sys.argv[1]
if not dir:
    print("must specify directory to first argument")

class_names = set()
output = Path("output")
output.mkdir(exist_ok=True)
filenames = []

for p in Path(dir).iterdir():
    records = []
    tree = ElementTree.parse(p)
    root = tree.getroot()
    folder = root.find("folder").text
    filename = root.find("filename").text
    filenames.append(filename)
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    for obj in root.findall("object"):
        class_name = obj.find("name").text
        class_names.add(class_name)
        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = min(width, int(bbox.find("xmax").text))
        ymax = min(height, int(bbox.find("ymax").text))
        records.append([class_name, xmin, ymin, xmax - xmin, ymax - ymin])

    with open(output / f"{Path(filename).stem}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(records)

random.shuffle(filenames)
train_idx = int(len(filenames) * 0.8)
train_filenames = filenames[:train_idx]
valid_filenames = filenames[train_idx:]

with open("train.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(
        [
            [train_filename, f"{Path(train_filename).stem}.csv"]
            for train_filename in train_filenames
        ]
    )


with open("valid.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(
        [
            [valid_filename, f"{Path(valid_filename).stem}.csv"]
            for valid_filename in valid_filenames
        ]
    )


with open("classes.txt", "w") as f:
    f.write("\n".join(class_names))
