from flask import Flask, render_template, session, request, redirect, flash
import re
EMAIL_REGEX = 	re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask (__name__)
app.secret_key="secret"

def hasNumbers(inputString):
	return bool(re.search(r'\d', inputString))

@app.route('/')
def survey():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create():

	if len(request.form['first_name']) < 1:
		flash("Fist name cant be blank")
		return redirect('/')
	elif hasNumbers(request.form['first_name']):
		flash("Your first name cant contain numbers")
		return redirect('/')
	elif len(request.form['last_name']) < 1:
		flash("Last name cant be blank")
		return redirect('/')
	elif hasNumbers(request.form['last_name']):
		flash("Last name cant contain numbers")
		return redirect('/')
	elif len(request.form['email']) < 1:
		flash("email cant be blank")
		return redirect('/')
	elif len(request.form['password']) < 1:
		flash("Password cant be blank")
		return redirect('/')
	elif len(request.form['confirmPassword']) < 1:
		flash("confirm password cant be blank")
		return redirect('/')
	elif len(request.form['password']) < 8:
		flash("password must be longer than 8 characters")
		return redirect('/')
	elif request.form['password'] != request.form['confirmPassword']:
		flash("Password must match confirm password")
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email format")
		return redirect('/')
	return render_template("created.html")
@app.route('/danger')
def danger():
	print("a user tried to visit/danger/we have redirected the user to /")
	return redirect("/")

if __name__ == ('__main__'):
	app.run(debug=True)