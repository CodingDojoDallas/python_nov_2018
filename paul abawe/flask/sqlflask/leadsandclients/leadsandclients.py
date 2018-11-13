from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def Dash():
    mysql = connectToMySQL("leadsdb")
    leads = mysql.query_db("SELECT * FROM leads")
    session['leads'] = leads
    print(leads)
    return render_template("index.html", leadsarr = leads)

app.run(debug=True)