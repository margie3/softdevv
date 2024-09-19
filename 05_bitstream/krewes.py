# Moyo Fagbuyi, Tim Ng, Margie Cao
# Systems Level Programming
# SoftDev
# K05 -- Working with str.split(), lists, and dictionaries
# 2024-09-17
# time spent: 1

import random

def duckies(str):
    devos = str.split("@@@") #seperating devos into elements of a list
    devos.remove("") #removing any empty entries
    info = []
    listdict = []
    for x in devos:
        info = x.split("$$$") #seperate each devos info (pd, name, ducky) into a dictionary
        dict = {"pd": 1, "devo": "temp", "ducky": "temp"}
        dict["pd"] = info[0]
        dict["devo"] = info[1]
        dict["ducky"] = info[2]
        listdict.append(dict) #appending dictionaries to a list
    x = random.randint(0, len(listdict)-1) #randomly selecting an index (devo) of the list
    print(listdict[x]["devo"] + " " + listdict[x]["pd"] + " " + listdict[x]["ducky"])
    
with open("krewes.txt", "r") as x:
    duckies(x.read())
#with statement ensures that the file is closed after operations are run