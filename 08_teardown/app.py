'''
Margie Cao
SoftDev
K08 -- Exploring Flask module
2024-09-20
time spent: 0.5
'''

'''
DISCO:
- print() is shown in terminal
- Flask uses a .run method to run the program

QCC:
0. Java: to make a new object you need a constructor (e.g. Flask(__name__)).
1. '/' differentiates different directories in the pathway. '/' by itself leads to the home directory.
2. This will print in the terminal.
3. __main__ or the name of the module
4. It will print out as html code. Clicking on the local host link, "No hablo queso!" pops up on the page.
5. My friend has seen similar language in JS for servers.
 ...

INVESTIGATIVE APPROACH:
Creating a virtual environemnt to download Flask and then running app.py.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?	```