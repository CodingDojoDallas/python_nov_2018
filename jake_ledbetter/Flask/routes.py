from flask import Flask
app = Flask (__name__)

print(__name__)
@app.route('/')
def hello_world():
	return "Hello World!"
@app.route('/dojo')
def dojo():
	return "Dojo!"
@app.route('/say/<name>')
def say(name):
	Name = name.capitalize()	
	return 'Hi ' + Name
@app.route('/repeat/<num>/<thing>')
def repeat(num,thing):
	string = ""
	for i in range(int(num)):
		string += thing + " "
	return string
if __name__ == "__main__":
	app.run(debug=True)