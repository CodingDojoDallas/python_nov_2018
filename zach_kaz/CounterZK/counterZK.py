from flask import Flask, session, redirect, render_template, request
app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def whattodo():
    if ('x' in session):
        print('here')
        session['x']+=1
    else:
        session['x']=1
    return render_template('counterhtml.html',x=session['x'])

@app.route('/bomb_session',methods=['POST'])
def bomb():
    session.clear()
    return redirect('/')
@app.route('/results', methods=['POST'])
def addtosession():
    session['x']+=1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 
