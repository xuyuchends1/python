import csv
import os.path


def readCSV(path):
    list = []
    a = ""
    with open(path) as f:
        a = f.read().replace("\n", "")
    list.extend(a.split(","))
    list.remove("")
    return list


path = input("please set csv file full path:")
if os.path.exists(path) == False:
    exit()
dir=os.path.dirname(path)
list = readCSV(path)
csv2=os.path.join(dir,"2.csv")
if os.path.exists(csv2):
    os.remove(csv2)
with open(csv2, mode="w") as f2:
    for x in list:
        f2.write(x + "\n")
