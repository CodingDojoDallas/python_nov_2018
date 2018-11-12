from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
from datetime import datetime
app = Flask(__name__)
app.secret_key='secretness'
@app.route('/')
def index():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT COUNT(leads.id),friends.last_name,friends.first_name FROM leads JOIN friends ON leads.friendsid=friends.id GROUP BY friends.last_name")
    if 'savethis' in session:
        displaythis=session['savethis']
    else:
        displaythis=all_friends
    if 'data' in session:
        date1= session['data']['date1']
        date2= session['data']['date2']   
    else: 
        date1="forever"
        date2="today"    
    return render_template('home.html', friends = displaythis,date1=date1,date2=date2)

@app.route('/resetdates', methods=['POST'])
def create():
    mysql = connectToMySQL("friendsdb")
    data = {
            'date1': request.form['date1'],
            'date2': request.form['date2']
    }
    query = "SELECT COUNT(leads.id),friends.last_name,friends.first_name FROM leads JOIN friends ON leads.friendsid=friends.id WHERE leads.created_at BETWEEN %(date1)s AND %(date2)s GROUP BY friends.last_name"
    new_friend_id = mysql.query_db(query, data)
    session['savethis']=new_friend_id
    session['data']=data
    print(session['savethis'])
    print(session['data'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
