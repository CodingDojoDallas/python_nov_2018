from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key='secretness'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
bcrypt = Bcrypt (app)

@app.route('/')
def start():

    return render_template('loginreghomeZK.html')

@app.route('/reg')
def show():
    return render_template('loginregcompleteZK.html')

@app.route('/logintest', methods=['post'])
def logincheck():
    mysql = connectToMySQL("friendsdb")
    email=request.form['email']
    data= {
        'email':email
    }
    checkstuff= mysql.query_db("SELECT * FROM `friendsdb`.`logins` WHERE `friendsdb`.`logins`.`email`=%(email)s",data)
    print(checkstuff)
    if bcrypt.check_password_hash(checkstuff[0]['pwhash'],request.form['pw'])==True:
        session['user']=checkstuff[0]['id']
        return redirect ('/home')
    else:
        flash("Your password didn't match. Please try again",'login')
        return redirect ('/')

@app.route('/home')
def homepage():
    return render_template('loginreghereZK.html')

@app.route('/test', methods=['post'])
def regtest():
    validreg=True
    print(request.form)
    if (len(request.form['firstname'])< 2) or (not NAME_REGEX.match(request.form['firstname'])):
        flash("First name must be at least two characters long and only be letters", 'firstname')
        validreg=False
    if (len(request.form['lastname'])< 2) or (not NAME_REGEX.match(request.form['lastname'])):
        flash("Last name must be at least two characters long and only be letters",'lastname')
        validreg=False
    if (len(request.form['email'])< 1) or (not EMAIL_REGEX.match(request.form['email'])):
        flash("Please enter a valid email address",'email')
        validreg=False
    if (len(request.form['pw'])<8):
        flash("Your password must contain at least eight characters",'password')
        validreg=False
    if (request.form['pw']!= request.form['pwconfirm']):
        flash("Your passwords did not match.",'confirmpassword')  
        validreg=False  
    if (validreg== False):
        return redirect('/')
    else:
        mysql = connectToMySQL("friendsdb")
        fn=request.form['firstname']
        ln=request.form['lastname']
        email=request.form['email']
        college=request.form['college']
        time=datetime.now().strftime('%Y-%m-%d')
        hash=bcrypt.generate_password_hash(request.form['pw'])
        data={
            'firstname':fn,
            'lastname':ln,
            'email':email,
            'college':college,
            'password':hash,
            'created_at':time,
            'updated_at':time
        }
        insertit = mysql.query_db("INSERT INTO `friendsdb`.`logins` (`first_name`,`last_name`,`email`,`college`,`pwhash`,`created_at`,`updated_at`) VALUES (%(firstname)s,%(lastname)s,%(email)s,%(college)s,%(password)s,%(created_at)s,%(updated_at)s)",data)  
        mysql = connectToMySQL("friendsdb")
        checkstuff= mysql.query_db("SELECT * FROM `friendsdb`.`logins` WHERE `friendsdb`.`logins`.`email`=%(email)s",data)
        session['user']=checkstuff[0]['id']

        return redirect ('/reg')

if __name__ == "__main__":
    app.run(debug=True)
