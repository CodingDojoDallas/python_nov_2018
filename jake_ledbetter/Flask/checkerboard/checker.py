from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def check8():
	return render_template("checker8.html")
@app.route('/<x>/<y>')
def checkXY(x,y):
	return render_template("checkerXY.html", x = int(x), y = int(y))
if __name__ == ("__main__"):
	app.run(debug=True)