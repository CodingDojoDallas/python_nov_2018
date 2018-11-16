from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def reg():
    return render_template('checker.html',x=8,y=8)

@app.route('/<x>/<y>')
def user(x,y):
    return render_template('checker.html',x=int(x),y=int(y))

if __name__=="__main__":
	app.run(debug=True) 