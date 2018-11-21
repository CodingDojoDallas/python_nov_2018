from flask_bcrypt import bcrypt
app = Flask(__name__)
app.secret_key = "Secret"
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z- ]+$')



@app.route('/')
def Form():
    if 'fname' not in session:
        session['fname'] = ""
    if 'lname' not in session:
        session['lname'] = ""
    if 'email' not in session:
        session['email'] = ""
    return render_template("index.html")



@app.route('/register', methods=['POST'])
def Register():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    mysql = connectToMySQL("mydb")

    query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password_hash)s);"

    data = { "username" : request.form['username'],
    "password_hash" : pw_hash }

    mysql.query_db(query, data)

    return redirect("/")


@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("mydb")
    query = "SELECT * FROM users WHERE username = %(username)s;"
    data = { "username" : request.form["username"] }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['id']
            return redirect('/success')
    flash("You could not be logged in")
    return redirect("/")