from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def playG1():
	return render_template("index.html")
@app.route("/play/<x>")
def playG2(x):
	return render_template("index2.html", x = int(x))
@app.route("/play/<x>/<Color>")
def playG3(x,Color):
	return render_template("index3.html", x = int(x), Color = Color)

if __name__ == "__main__":
	app.run(debug=True)
