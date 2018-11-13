from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app= Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def home():
	mysql = connectToMySQL('friendsdb')	
	query= "SELECT * from friendsdb.friends"
	allfriend=mysql.query_db(query)
	print(allfriend)
	return render_template('friends.html' , allfriend=allfriend)

@app.route('/add', methods=["POST"])
def add():
	
	if len(request.form['fname']) < 1:
		flash("You must have a first name to continue!",'fname')
		return redirect('/')
	if len(request.form['lname']) < 1:
		flash("You must have a last name to continue!",'lname')
		return redirect('/')
	if len(request.form['occu']) < 1:
		flash("You must have a job to continue!",'occu')
		return redirect('/')
	mysql = connectToMySQL('friendsdb')	
	query= "INSERT into friendsdb.friends(first_name, last_name, occupation) values (%(fname)s, %(lname)s, %(occu)s);" 
	data={
		'fname':request.form['fname'],
		'lname':request.form['lname'],
		'occu':request.form['occu']
		}
	mysql.query_db(query, data)
	return redirect('/')

if __name__=='__main__':
    app.run(debug=True) 