from os import scandir, remove
from random import shuffle
from json import dumps

IGNORED_FOLDERS = [".git", ".github"]
AGGREGATED_JSON_FILE = "students.json"
AGGREGATED_MKDOWN_FILE = "students.md"

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
    remove(AGGREGATED_JSON_FILE)
except:
    pass

# Write Aggregated File
with open(AGGREGATED_JSON_FILE, "w") as fp:
    fp.write(dumps({"students": folders}))

students_md = """
## Students
List of students who took the course

"""

for student in folders:
    students_md += f"[{student}]({student})  \n"

# Try to Delete current Students Md File
try:
    remove(AGGREGATED_MKDOWN_FILE)
except:
    pass

# Write Aggregated File
with open(AGGREGATED_MKDOWN_FILE, "w") as fp:
    fp.write(students_md)
