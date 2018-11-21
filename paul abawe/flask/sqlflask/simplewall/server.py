from flask import Flask, session, render_template, flash, request, redirect
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z- ]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsKey!"


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/createUser", methods=["POST"])
def create():
    mysql = connectToMySQL("simplewall")
    emailquery = "SELECT * FROM users WHERE email = %(email)s;"
    emaildata = {"email": request.form["email"]}
    emailcheck = mysql.query_db(emailquery, emaildata)

    if len(request.form["first_name"]) < 1:
        flash("First name cannot be blank!", category="first_name")
    elif not NAME_REGEX.match(request.form["first_name"]):
        flash("Name cannot contain special characters!", category="first_name")

    if len(request.form["last_name"]) < 1:
        flash("Last name cannot be blank!", category="last_name")
    elif not NAME_REGEX.match(request.form["last_name"]):
        flash("Name cannot contain special characters!", category="last_name")

    if len(request.form["email"]) < 1:
        flash("Email cannot be blank!", category="email")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address!", category="email")
    elif emailcheck:
        flash("Email already in use!", category="email")

    if len(request.form["password"]) < 7:
        flash("Password must be at least 8 characters!", category="password")
    elif request.form["password"] != request.form["confirmpassword"]:
        flash("Passwords must match!", category="confirmpassword")

    if "_flashes" in session.keys():
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        session['email'] = request.form['email']
        session['logged_in'] = True
        mysql = connectToMySQL("simplewall")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password_hash": pw_hash,
        }
        result = mysql.query_db(query, data)
        print(result)

        mysql = connectToMySQL("loginregistration")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        dataemail = {"email": request.form["email"]}
        result2 = mysql.query_db(query, dataemail)

        session["userid"] = result
        session["name"] = data["first_name"]

        return redirect("/wall")


@app.route("/login", methods=["POST"])
def login():
    mysql = connectToMySQL("simplewall")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {"email": request.form["email"]}
    result = mysql.query_db(query, data)
    print(result)

    if len(request.form['email']) < 1:
        flash("Email required", "login_status")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("email must be valid!", "login_status")
    
    if len(request.form['password']) < 1:
        flash("Password required", "login_status")


    if result:  # is username in database?
        print("whoooo")
        if bcrypt.check_password_hash(result[0]["password"], request.form["password"]):
            session['email'] = request.form['email']
            session['logged_in'] = True
            session["userid"] = result[0]["id"]
            session["name"] = result[0]["first_name"]
            print("hello")
            return redirect("/wall")

    flash("You could not be logged in")
    return redirect("/")



@app.route("/wall")
def wall():
    if session['logged_in'] == False:
        flash("Please Log In", "status")
        return redirect('/')

    elif 'email' not in session:
        flash('Please Log in', "status")
        return redirect("/")

    else:
        unique_session_id = session["userid"]
        mysql = connectToMySQL("simplewall")
        number_of_messages=mysql.query_db("Select COUNT(recipient_id) from messages where recipient_id={}".format(unique_session_id))

        unique_session_id = session["userid"]
        mysql = connectToMySQL("simplewall")
        user_messages=mysql.query_db("SELECT * from messages where recipient_id ={}".format(unique_session_id))

        unique_session_id = session["userid"]
        mysql = connectToMySQL("simplewall")
        receivers=mysql.query_db("SELECT * from users where id !={}".format(unique_session_id))

        unique_session_id = session["userid"]
        mysql = connectToMySQL("simplewall")
        senders_name=mysql.query_db("select * from messages join users on users.id = messages.users_id where users_id1 ={}".format(unique_session_id))

        unique_session_id = session["userid"]
        mysql = connectToMySQL("simplewall")
        messagescol=mysql.query_db("SELECT COUNT(*) FROM simplewall.messages where users_id={}".format(unique_session_id))
        print(messagescol, "/////////////////////")

        return render_template('wall.html', number_of_messages = number_of_messages, user_messages = user_messages, receivers = receivers, senders_name = senders_name, messagescol = messagescol )


@app.route("/send/<x>", methods=["POST"])
def post(x):

    mysql = connectToMySQL("simplewall")
    query = "INSERT INTO messages ( message, sender_id, recipient_id, created_at, updated_at) VALUES (%(message)s, %(sender_id)s, %(recipient_id)s, NOW(), NOW());"
    data = {
            'message': request.form['message'],
            'sender_id': session["id"],
            'recipient_id' : x ,
    }
    message_sent=mysql.query_db(query, data)

    return redirect('/wall')





@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
