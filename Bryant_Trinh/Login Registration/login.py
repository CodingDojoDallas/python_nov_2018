from flask import Flask, render_template, session, request, redirect, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app) 

@app.route("/")
def index():
	return render_template("login.html")
   
@app.route("/register", methods=['POST'])
def reserve():
	if len(request.form['fname']) <= 2:
		flash("First name must have at least 2 letters!", 'fname')
	if len(request.form['lname']) <= 2:
		flash("Last name must have at least 2 characters!", 'lname')
	if len(request.form['email']) < 2:
		flash("Invalid Email Address!", 'email')
	if (not NAME_REGEX.match(request.form['fname'])):
		flash("First name must have only letters., 'fname")
	if (not NAME_REGEX.match(request.form['lname'])):
		flash("Last name must have only letters., 'lname")
	if (len(request.form['email']) < 2) or (not EMAIL_REGEX.match(request.form['email'])):
		flash("Invalid Email Address!", 'email')
	if (len(request.form['pass'])<8):
		flash("Your password must contain at least eight characters",'pass')
	if (request.form['pass']!= request.form['cpass']):
		flash("Your passwords did not match.",'confirmpassword')
	if '_flashes' in session.keys():
		return redirect("/")
	else:
		mysql = connectToMySQL("emaildb")
		fn=request.form['fname']
		ln=request.form['lname']
		email=request.form['email']
		session["fname"] = request.form['fname']
		session['lname'] = request.form['lname']
		time=datetime.now().strftime('%Y-%m-%d')
		hash=bcrypt.generate_password_hash(request.form['pass'])
		data={
			'firstname':fn,
			'lastname':ln,
			'email':email,
			'password':hash,
			'created_at':time,
			'updated_at':time
		}
		register=mysql.query_db('INSERT INTO emaildb.users(first_name, last_name, email, hash, created_at, updated_at) values (%(firstname)s,%(lastname)s,%(email)s,%(password)s,%(created_at)s,%(updated_at)s);' , data)
		mysql.query_db(register, data)
		return redirect("/success")

@app.route('/login', methods=['POST'])
def login():
	mysql = connectToMySQL("emaildb")
	email=request.form['email']
	data={
		'email': email,
	}
	verify= mysql.query_db("SELECT * FROM emaildb.users WHERE email = %(email)s;",data)
	if bcrypt.check_password_hash(verify[0]['hash'],request.form['pass'])==True:
		session['user']=verify[0]['user']
		return redirect ('/loginsuccess')
	else:
		flash("Your email or password didn't match or might not exist. Please try again",'login')
		return redirect ('/')

@app.route("/success")
def success():
	return "Thank you " + session["fname"] + session['lname'] + " for registering. You are now free to use to site to and all its functions."

@app.route('/loginsuccess')
def logsuccess():
	return "Thank you for logging in. You are free to use the site normally."  

if __name__ == "__main__":
	app.run(debug=True)