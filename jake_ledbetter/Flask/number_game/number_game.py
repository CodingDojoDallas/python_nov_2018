from flask import Flask , render_template, request, redirect, session, flash
import random

app=Flask(__name__)
app.secret_key='Secret'

@app.route('/')
def index():
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    return render_template("index.html", message=session['message'] )

@app.route('/guess', methods=['POST'])
def guess():

    guessNumber = int(request.form['number'])
    if guessNumber== session['number']:
        session['message']= "You got it!!! "+ str(guessNumber) +" was the number. Click reset to play again."
    elif guessNumber > session['number']:
        session['message']= 'Your guess is too high. Try again.'
    elif guessNumber< session['number']:
        session['message']= 'Your guess is too low. Try agian.'
    return redirect('/')
@app.route('/reset')
def reset():
    session.pop("number")
    session.pop("message")
    return redirect('/')
app.run(debug=True)