# Margie, Jayden, Naf
# SoftDev
# Sep 30 2024

import csv
import random

with open('occupations.csv', newline='') as csvfile: # reads the csv file using python's csv import
    occupations = csv.reader(csvfile)
    dict = {} # initatizes a new dictionary
    for row in occupations:
        if (row[0] != 'Job Class') and (row[0] != 'Total'): # removes the first and last keys
            dict.update({row[0]:float(row[1])}) # updates the dictionary with the occupations as keys and the percentage as values.
    
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/wdywtbwygp")
def occupations():
    title = "GOOGle - Margie Cao, Jayden Zhang, Nafiyu Murtaza<br>Occupation of the Day: " # creates the starting string
    x = random.uniform(0.0,99.8)
    for key, value in dict.items():
        x = x - value # each key has a range and this subtracts until it is chosen
        if x <= 0:
            finalText = finalText + key + "<br>" # adds the randomly selected occupation html
            break
    finalText = finalText + "<table>"
    for key, value in dict.items(): # appends each key in the list of keys into the finalText string to return as one big string
        finalText = finalText + "<tr> <td style='border: 1px solid black'>" + key + "</td> <td style='border: 1px solid black'>" + str(value) + "</td> </tr>"  # uses the <br> command which is commonly seen in html which is similar to \n
    finalText = finalText + "</table>"
    return finalText


if __name__ == "__main__":
    app.debug = True
    app.run()   