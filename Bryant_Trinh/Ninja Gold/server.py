from flask import Flask, render_template, request, redirect, session

import random
from datetime import datetime, date, time

app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
	if "currentgold" not in session:
		session["currentgold"]=0
	if "location" not in session:
		session["location"]=0
	if "findgold" not in session:
		session["findgold"]=0
	if "string" not in session:
		session["string"]=""

	return render_template('index.html' , currentgold=session["currentgold"] , string=session["string"])

@app.route('/process_money' , methods=["POST"])
def process():
	if request.form["location"] == "farm":
		session["findgold"] = random.randrange(10,21)
		session["currentgold"] += int(session["findgold"])
		session["string"] += "\n" + "You earned " + str(session["findgold"]) + "golds from the farm! " + str(datetime.today())
	if request.form["location"] == "cave":
		session["findgold"] = random.randrange(5,11)
		session["currentgold"] += int(session["findgold"])
		session["string"] += "\n" + "You earned " + str(session["findgold"]) + "golds from the cave! " + str(datetime.today())
	if request.form["location"] == "farm":
		session["findgold"] = random.randrange(2,6)
		session["currentgold"] += int(session["findgold"])
		session["string"] += "\n" + "You earned " + str(session["findgold"]) + "golds from the house! " + str(datetime.today())
	if request.form["location"] == "casino":
		session["findgold"] = random.randrange(-50,51)
		session["currentgold"] += int(session["findgold"])
		if session["findgold"] > -1:
			session["string"] += "\n" + "You walked into a casino and won " + str(session["findgold"]) + " golds. YAY!! " + str(datetime.today())
		else:
			session["string"] += "\n" + "You walked into a casino and lost" + str(session["findgold"]) + " golds. OUCH!! " + str(datetime.today())

	return redirect('/')		

@app.route('/reset' , methods=["POST"])
def reset():
	if "currentgold" in session:
		session["currentgold"] = 0

	return redirect('/')
		

if __name__=='__main__':
    app.run(debug=True) 