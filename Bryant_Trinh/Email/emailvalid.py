from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="ThisIsSecret"       

@app.route('/')
def home():
	if "email" not in session:
		session["email"]=""
	return render_template('email.html')


@app.route('/valid', methods=['POST'])
def validation():
	session['email'] = request.form["email"]
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!", 'email')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email address is not valid", 'email')
		return redirect('/')
	time=datetime.now()
	data={
		'email':request.form['email'],
		'created_at': time
		}
	mysql = connectToMySQL('email')	
	query= "SELECT email FROM email.users where email=%(email)s;"
	same=mysql.query_db(query,data)
	print(same)
	if len(same) > 0:
		flash("Email address is already in use. Please use a different email.", 'email')
		return redirect('/')
	else:
		mysql = connectToMySQL('email')
		query="INSERT into email.users (email,created_at) values (%(email)s,%(created_at)s);"
		
		
		mysql.query_db(query, data)
		return redirect('/success')
	print(same)
	

@app.route('/success')
def success():
	emadd = session['email']
	mysql = connectToMySQL('email')	
	query= "SELECT email, created_at from email.users"
	email=mysql.query_db(query)
	return render_template('success.html' , emails=email, emadd=emadd)


if __name__ == "__main__":
    app.run(debug=True)