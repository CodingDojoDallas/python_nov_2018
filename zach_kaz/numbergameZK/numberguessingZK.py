from flask import Flask, redirect, render_template, session, request
import random
app= Flask(__name__)
app.secret_key="secretness"

@app.route('/')
def home():
    if ('number' not in session):
        session['number']=random.randrange(0, 101)
    if ('display' in session):
        if (session['display']=='yes'):
            dis=1
        else:
            dis=0
    else:
        dis=0
    if ('status' not in session):
        session['status']=0
    print(session['status'])
    numberguess=int(session['status'])
    return render_template('numberguessing.html',dis=dis,numberguess=numberguess)

@app.route('/answer', methods=['POST'])
def getanswer():
    session['display']='yes'
    session['status']=0
    return redirect('/')

@app.route('/endsession', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')

@app.route('/guess', methods=['POST'])
def guess():
    print('guess works')
    if int(session['number'])==int(request.form['numberguess']):
        session['status']='1'
    elif int(session['number'])>int(request.form['numberguess']):
        session['status']='2'
    else:
        session['status']='3'
    print(session['status'])
    return redirect('/')
    



if __name__=="__main__":
    app.run(debug=True) 
