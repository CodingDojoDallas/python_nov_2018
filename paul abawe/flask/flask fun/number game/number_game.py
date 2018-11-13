from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key ='thisIsSecret'

print(__name__)
@app.route('/')
def Index():
    if 'rand' not in session:
        session['rand'] = random.randrange(1,101)
    print(session['rand'])
    return render_template('number_game.html', rand = session['rand'])

@app.route('/guess', methods = ['POST'])
def Guess():
    guess = request.form['guess']
    if int(guess) < session['rand']:
        return render_template('too_low.html')
    if int(guess) > session['rand']:
        return render_template('too_high.html')
    if int(guess) == session['rand']:
        return render_template('play_again.html')
@app.route('/new', methods = ['POST'])
def New():
    session['rand'] = random.randrange(1,101)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)