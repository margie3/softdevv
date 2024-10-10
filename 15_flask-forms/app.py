'''
Margie Cao, Moyo Fagbuyi
M&M
SoftDev
K15 -- Creating a Flask App
2024-10-08
Time Spent: 2 hours
'''
    
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST']) # home route
def starting_page():
    return render_template("login.html")
    
@app.route("/response", methods=['GET', 'POST'])
def response_page():
    request = request.method
    if request.method == "GET": 
        username = request.args["username"] #taking data from args library
    elif request.method == "POST":
        username = request.form["username"] #different from get method, stores in form library
    breakdown = "the GET method is HTML's default method and checks the args dictionary for the data inputted. This data can be seen in the URL unlike the POST method which stores the data in a form dictionary by sending it to the server."        
    return render_template("response.html", request = request, username = username, breakdown = breakdown)

if __name__ == "__main__": 
    app.debug = True # allows for constant refreshing
    app.run() # runs the app
