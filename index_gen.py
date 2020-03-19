#!/usr/bin/env python3

import os

seperator = "  "
return_strings = []

# Based on https://stackoverflow.com/a/16974952
# Thank you based Ajay && based zaooza

for root, dirs, files in os.walk(u"."):
    path = root.split(os.sep)

    if ".git" in path:
        continue

    if path != ["."]:
        return_strings.append((len(path) - 2) * seperator + "* " + os.path.basename(root))
    for file in files:
        if file not in ["README.md", "index.md", "index_gen.py"]:
            link = "/".join([root, file])
            prefix = (len(path) -1) * seperator + "* "
            file_nice_name = file.split(".")[0]
            return_strings.append(f"{prefix}[{file_nice_name}]({link})")

with open("index.md", "w") as index_file:
    return_strings = map(lambda x: x + '\n', return_strings)
    index_file.writelines(return_strings)

