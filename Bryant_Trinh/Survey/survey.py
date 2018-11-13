from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/', methods=['GET'])
def index():
	if "name" not in session:
		session["name"]=""
	if "location" not in session:
		session["location"]=""
	if "info" not in session:
		session["info"]=""

	return render_template('survey1.html')

@app.route('/result', methods=['POST'])
def results():
	if len(request.form['name']) < 1:
		flash("You must have a name to continue!" )
	elif len(request.form['name']) > 120:
		flash("Your name is too long!",'name')
	if len(request.form['location']) < 1:
		flash("You must work somewhere to take this survey.",'location')
	if len(request.form['info']) < 1:
		flash("Everybody has a thought! Put yours in.",'info')
	elif len(request.form['info']) > 120:
		flash("You have too much comments, 120 characters max",'info')
	if '_flashes' in session.keys():
		return redirect("/")
	return render_template("surveyresults.html")

@app.route('/danger')
def danger():
	print("a user tried to visit /danger.  we have redirected the user to the homepage")
	return redirect('/')

if __name__=="__main__":
	app.run(debug=True) 