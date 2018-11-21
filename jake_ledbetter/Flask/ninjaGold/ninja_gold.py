from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime, date, time
app = Flask(__name__)
app.secret_key="Secret"
@app.route('/')
def count():
	if "current_gold" not in session:
		session["current_gold"]=0
	if "location" not in session:
		session["location"]=0
	if "findgold" not in session:
		session['findgold']=0
	if "string" not in session:
		session['string']=''
	return render_template("index.html", current_gold=session["current_gold"], string=session["string"])

@app.route('/process_money', methods=["POST"])
def process():
	if request.form["location"] == "farm":
		session["findgold"] = random.randrange(10,21)
		session["current_gold"] += int(session["findgold"])
		session["string"] += "\n" + "you earned " + str(session["findgold"])+" gold from the farm! " +str(datetime.today()) + " ---- "
	if request.form["location"] == "cave":
		session["findgold"] = random.randrange(5,11)
		session["current_gold"] += int(session["findgold"])
		session["string"] += "\n" + "you earned " + str(session["findgold"])+" gold from the cave! " +str(datetime.today()) + " ---- "
	if request.form["location"] == "house":
		session["findgold"] = random.randrange(2,6)
		session["current_gold"] += int(session["findgold"])
		session["string"] += "\n" + "you earned " + str(session["findgold"])+" gold from the house! " +str(datetime.today()) + " ---- "
	if request.form["location"] == "casino":
		session["findgold"] = random.randrange(-50,51)
		session["current_gold"] += int(session["findgold"])
		if session["current_gold"]<0:
			session['current_gold']=0
		session["string"] += "\n" + "you earned " + str(session["findgold"])+" gold from the casino! " +str(datetime.today()) + " ---- "

	return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)   

