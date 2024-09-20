# Moyo Fagbuyi, Margie Cao
# M & M
# SoftDev
# K06 -- Reading CSVs and storing them into dictionaries
# 2024-09-17
# time spent: 41 mins
import random

with open('occupations.csv','r') as text:
    data = text.readlines()
    #turnss file into a string  
    list = []
    data[0] = ""
    #removes the title lines
    for x in data :
        if not x  == "":
            str = x.split(",")
            list.append({str[0] : str[1][:-1]})
            #for every line
            #if the line has data,
            #make a dict with the job as key and % as value
    x = random.randint(0, 998)
    for dict in list:
        for key in dict:
            print(dict)
#             print(dict.get(key))
#             x = x - float(dict.get(key))*10
#             if x < 0:
#                 print(key)
#                 break;
        
    
'''

DISCO:

QCC:

- Is there a more efficent way to do the distrubition rahter than
having a list with 100 entries based on how common the job is?

HOW THIS SCRIPT WOKRS:


'''