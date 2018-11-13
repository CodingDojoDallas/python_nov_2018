from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    print('AFOOIEJFEWOIFJWEUHUVEUBWIE')
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/flask')
def say():
    return "Hi Flask"

@app.route('/saythis/<name>')
def saythis(name):
    return "Hi "+name

@app.route('/repeat/<x>/<word>')
def repeatword(x,word):
    return int(x)*word

@app.route('/play/<x>/<color>')
def coloredboxes(x,color):
    return render_template('hellohtml.html',numberboxes=int(x),color=color)

@app.route('/play/<x>/')
def boxes(x):
    return render_template('hellohtml.html',numberboxes=int(x))

if __name__=="__main__":
    app.run(debug=True)