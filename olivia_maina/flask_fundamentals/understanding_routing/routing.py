from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!' 

@app.route('/say/<name>')
def say(name):
    return 'Hi ' + str(name)

@app.route('/repeat/35/hello')
def repeat():
    return 'Hello ' * int(35)

@app.route('/repeat/99/dogs')
def  dogs():
    return "Dog's" * int(99)

if __name__ == "__main__":
    app.run(debug=True)
