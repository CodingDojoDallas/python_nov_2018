from flask import Flask, session, render_template, flash, request, redirect
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "HelloClang01"
mysql = connectToMySQL('mydb')
print("All of the user information", mysql.query_db("SELECT * FROM walluser;"))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	mysql = connectToMySQL('mydb')
	query = "SELECT * FROM walluser WHERE email = %(email)s"
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
		query = "INSERT INTO walluser (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(hashed_pass)s );"
		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'hashed_pass': hashed_pass
		}
		mysql = connectToMySQL('mydb')
		newUser = mysql.query_db(query, data)
		mysql = connectToMySQL("mydb")
		query = "SELECT * FROM walluser WHERE email = %(email)s;"
		data = {
			'email': session['email']
		}
		return_user = mysql.query_db(query,data)
		session['id'] = return_user[0]['id']
		flash("You have succeded in registering")
		return redirect('/wall')

@app.route('/test', methods=['POST'])
def test():

	password = request.form['passLog']
	email = request.form['emailLog']
	session['email'] = email
	mysql = connectToMySQL("mydb")
	query = "SELECT * FROM walluser WHERE email = %(email)s;"
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
			session['id'] = check[0]['id']
			return redirect('/wall')
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
	name = mysql.query_db("SELECT * FROM walluser where email == request.form['emailLog']")
	return render_template('loggedIn.html', name = name)
@app.route('/wall')
def wall():
	mysql = connectToMySQL("mydb")
	query = "SELECT id, first_name, last_name, email FROM walluser WHERE id != %(id)s;"
	data = {
		'id': session['id']
	}
	others = mysql.query_db(query, data)

	mysql = connectToMySQL("mydb")
	query = "SELECT message.id, walluser.id, message.messageText, message.user_id, walluser.first_name, message.sentAt FROM message JOIN walluser ON walluser.id = message.user_id WHERE message.sentTo = %(id)s OR walluser.id = %(id)s ORDER BY message.sentAt DESC"
	data = {
		'id': session['id']
	}
	messages_return = mysql.query_db(query, data)



	return render_template("loggedIn.html", others= others, messages = messages_return)

@app.route('/send',methods=['POST'])
def send():
	print(request.form)
	message = request.form['message']
	rec_id = request.form['rec_id']
	mysql = connectToMySQL("mydb")
	print("BEEEEEEEEEEEEEEEEEEEEEEEEEEEFOOOOREEEEEEEEEEEEEE")
	query = "INSERT INTO message (user_id,sentTo,messageText,sentAt) VALUES(%(user_id)s, %(sentTo)s, %(messageText)s, NOW());"
	data = {
		'user_id': session['id'],
		'sentTo': rec_id,
		'messageText': message
	}
	print("AAAAAAAAAAAAAAAAAAAAAAAAAAAFFFFFFFFFFFTERRRRRRRRR")
	insertMessage = mysql.query_db(query, data)
	print(session['id'])
	return redirect('/wall')

@app.route('/delete', methods=['POST'])
def delete():
	mysql = connectToMySQL("mydb")
	id = request.form['delete']
	query = "DELETE FROM message WHERE id = %(id)s"
	data ={
		'id':id
	}
	deleteMsg = mysql.query_db(query,data)
	return redirect('/wall')

@app.route('/logOut')
def logOut():
	session.clear()
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)