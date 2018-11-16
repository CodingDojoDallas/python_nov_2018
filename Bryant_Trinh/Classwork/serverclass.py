from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
app = Flask(__name__)        
bcrypt = Bcrypt(app)

@app.route('/')
def home():
	mysql = connectToMySQL('friends')
	result=mysql.query_db("Select * from animal")
	print(result)
	return render_template(index.html)

@app.route('/process', methods=['POST'])
def proces():
	query= "Insert into animal (name, category, date_birth) values (%(name)s, %(category)s, %(date_birth)s)"
	data={
	'name':request.form['name'],
	'category':request.form['category'],
	'date_birth':datetime.strptime(request.form['dob'],"%y-%m-%d").date().strftime("%y-%m-%d")
	}
#print("all the users", mysql.query_db("SELECT * FROM users;"))
	mysql.query_db(query,data)
	return redirect('/home')

@app.route('/home')
def f():
	return render_template('success.html')
if __name__ == "__main__":
    app.run(debug=True)