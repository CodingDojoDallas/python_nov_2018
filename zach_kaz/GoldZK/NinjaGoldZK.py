from flask import Flask, render_template, request, session, redirect
import random
import datetime
app=Flask(__name__)
app.secret_key="secret"

@app.route('/')
def findgold():
    if 'gold' not in session:
        session['gold']=0
    if 'narrative' not in session:
        session['narrative']=[]
    gold=session['gold']        
    chunktext=session['narrative']
    for i in range(0,int(len(chunktext)/2)):
        chunktext[i], chunktext[int(len(chunktext))-i-1]=chunktext[int(len(chunktext))-i-1], chunktext[i]
    print(chunktext)
    x=''.join(chunktext)
    return render_template('goldpage.html', gold=gold,chunktext=x)

@app.route('/reset', methods=['post'])
def endsession():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['post'])
def makegold():
    if request.form['building']=='farm':
        session['addgold']=random.randrange(10,50)
        session['gold']+=session['addgold']
        session['narrative'].append("<div class='farm narrationline'>You farmed for "+str(session['addgold'])+" gold. You know have "+str(session['gold'])+" gold total.</div>")
    if request.form['building']=='cave':
        session['addgold']=random.randrange(5,10)
        session['gold']+=session['addgold']
        session['narrative'].append("<div class='cave narrationline'>You entered the cave and found "+str(session['addgold'])+" gold. You know have "+str(session['gold'])+" gold total.</div>")
    if request.form['building']=='house':
        session['addgold']=random.randrange(2,5)
        session['gold']+=session['addgold']
        session['narrative'].append("<div class='house narrationline'>You pillaged a poor villager for "+str(session['addgold'])+" gold. You know have "+str(session['gold'])+" gold total.</div>")
    if request.form['building']=='casino':
        session['addgold']=random.randrange(-50,50)
        session['gold']+=session['addgold']
        if session['addgold']>0:
            session['narrative'].append("<div class='casino won narrationline'>You won "+str(session['addgold'])+" gold. You know have "+str(session['gold'])+" gold total.</div>")
        else:
            session['narrative'].append("<div class='casino lost narrationline'>You lost "+str(session['addgold']*-1)+" gold! You know have "+str(session['gold'])+" gold total.</div>")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 
