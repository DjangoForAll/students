from os import scandir, remove
from random import shuffle
from json import dumps

IGNORED_FOLDERS = [".git", ".github"]
AGGREGATED_FILE = "students.json"

folders = []

# Scan folder and get all folders
for obj in scandir("."):
    if not obj.is_dir():
        continue
    folder = obj.name
    if folder in IGNORED_FOLDERS:
        continue
    folders.append(folder)

# Shuffle folders so that the order keeps changing
shuffle(folders)

# Try to Delete current json
try:
    remove(AGGREGATED_FILE)
except:
    pass

# Write Aggregated File
with open(AGGREGATED_FILE, "w") as fp:
    fp.write(dumps({"students": folders}))
