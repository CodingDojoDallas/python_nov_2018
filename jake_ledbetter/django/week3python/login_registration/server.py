from flask import Flask, session, render_template, flash, request, redirect
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "HelloClang01"
mysql = connectToMySQL('mydb')
print("All of the user information", mysql.query_db("SELECT * FROM login;"))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	mysql = connectToMySQL('mydb')
	query = "SELECT * FROM login WHERE email = %(email)s"
	data = {
		'email': request.form['email']
	}
	result = mysql.query_db(query, data)
	print(result)

	if len(result) != 0:
		flash("This email is already in the database.",'error')

	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email format.",'error')

	if len(request.form['first_name']) <1:
		flash("You left your first name blank.",'error')

	elif not request.form['first_name'].isalpha():
		flash("You put numbers in your first name.",'error')

	if len(request.form['last_name']) <1:
		flash("You left your last name blank.",'error')

	elif not request.form['last_name'].isalpha():
		flash("You put numbers in your last name.",'error')

	if len(request.form['password']) < 1:
		flash("You left your password blank.",'error')

	elif len(request.form['password']) < 8:
		flash("Your password must be greater than 8 characters.",'error')

	if '_flashes' in session.keys():
		return redirect('/')
	else:

		hashed_pass = bcrypt.generate_password_hash(request.form['password'])
		print(hashed_pass)
		session['email'] = request.form['email']
		session['loggedIn'] = True
		session['first_name'] = request.form['first_name']
		myql = connectToMySQL('mydb')
		query = "INSERT INTO login (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(hashed_pass)s );"
		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'hashed_pass': hashed_pass
		}
		mysql = connectToMySQL('mydb')
		mysql.query_db(query, data)
		flash("You have succeded in registering")
		return redirect('/success')

@app.route('/test', methods=['POST'])
def test():

	password = request.form['passLog']
	email = request.form['emailLog']
	mysql = connectToMySQL("mydb")
	query = "SELECT * FROM login WHERE email = %(email)s;"
	data = {
		'email': email
	}
	check = mysql.query_db(query,data)
	print (check)
	if check:
		if bcrypt.check_password_hash(check[0]['password'], request.form['passLog']):
			session['email'] = request.form['emailLog']
			session['loggedIn'] = True
			mysql = connectToMySQL("mydb")
			session['first_name'] = check[0]['first_name']
			return redirect('/success')
		else:
			flash('Could not be logged in','error')
			return redirect('/')
	else:
		return redirect('/')
@app.route('/success')
def success():
	if session['loggedIn'] == False:
		flash('not logged in')
		return redirect('/')

	elif 'email' not in session:
		flash("please log in")
		return redirect('/')
	
	mysql = connectToMySQL('mydb')		
	name = mysql.query_db("SELECT * FROM login where email == request.form['emailLog']")
	return render_template('loggedIn.html', name = name)

@app.route('/logOut')
def logOut():
	session['loggedIn'] = False
	session.pop('email')
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)