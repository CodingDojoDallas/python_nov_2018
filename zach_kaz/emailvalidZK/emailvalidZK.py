from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re
app = Flask(__name__)
app.secret_key='secretness'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def start():
    print(flash)
    return render_template('emailvalidZK.html')

@app.route('/test', methods=['post'])
def index():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("EMAIL IS NOT VALID")
        print("flAShmessAGE SHOULD E DISPLAYING!!!!!!!")
        return redirect ('/')
    mysql = connectToMySQL("friendsdb")
    email=request.form['email']
    time=datetime.now().strftime('%Y-%m-%d')
    data={
        'email':email,
        'created_at':time,
        'updtaed_at':time
    }
    print(data)
    insertit = mysql.query_db("INSERT INTO `friendsdb`.`friends` (`created_at`,`email`,`updated_at`) VALUES (%(created_at)s,%(email)s,%(created_at)s)",data)  
    return redirect ('/success')

@app.route('/success')
def show():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT email,created_at FROM friends")    
    return render_template('emailvalidsuccessZK.html', friends=all_friends)

if __name__ == "__main__":
    app.run(debug=True)
