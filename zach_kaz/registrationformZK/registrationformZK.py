from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "thisissecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
@app.route('/')
def index():
    return render_template("registrationhome.html")
@app.route('/register', methods=['POST'])
def DJresults():
    validreg=True
    if len(request.form['first_name'])< 1:
        flash("Please tell us your firstname.")
        validreg=False
    if not NAME_REGEX.match(request.form['first_name']):
        flash("Your name cannot contain any numerals")
        validreg=False
    if len(request.form['last_name'])< 1:
        flash("Please tell us your lastname.")
        validreg=False
    if not NAME_REGEX.match(request.form['first_name']):
        flash("Your name cannot contain any numerals")
        validreg=False
    if len(request.form['email'])< 1:
        flash("Please tell us your email.")
        validreg=False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address.")
        validreg=False
    if len(request.form['password'])< 1:
        flash("Please create a password.")
        validreg=False
    elif len(request.form['password'])<8:
        flash("Your password must be at least 8 characters long")
        validreg=False
    if (request.form['password']!= request.form['confirmpw']):
        flash("Your passwords did not match.")  
        validreg=False  
    if (validreg== False):
        flash("Please try again")
        return redirect('/reg')
    else:
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        session['password']=request.form['password']
        flash("You registration is complete. Thank you for joining us for ArtCon 2018")
        return redirect('/reg')

@app.route('/reg')
def registered():
    return render_template('regcomplete.html')

if __name__=="__main__":
    app.run(debug=True) 
