#yes this is an abomination, I dont care, it does the job :)

import sys

if len(sys.argv) != 3:
    print("Bad arguments, usage: python allMerger.py <allFile> <toImportFile>")

allFile = sys.argv[1]
importFile = sys.argv[2]

with open(importFile, "r") as f:
    lines = f.readlines()
    for i in lines:
        if i not in open(allFile).read():
            i = i.replace("\"", "")
            if i[0] == "\"" and i[len(i)-1] == "\"":
                i = i[1:]
                i = i[:-1]
            if i[0] == "“" and i[len(i)-1] == "“":
                i = i[1:]
                i = i[:-1]                
            if i[0] == "'" and i[len(i)-1] == "'":
                i = i[1:]
                i = i[:-1]       
            with open(allFile, "a") as allF:
                allF.write(i)

