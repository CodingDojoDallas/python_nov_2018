from flask import Flask, render_template
app= Flask(__name__)

print(__name__)

@app.route("/")
def HelloWorld():
	return "Hello World"

@app.route("/play")
def play():
	return render_template("index.html")

@app.route("/play/<num>")
def playnum(num):
	return render_template("index.html", boxnum=int(num))

@app.route("/play/<num>/<color>")
def playcolor(num,color):
	return render_template("index.html", boxnum=int(num), color=color)

if __name__=="__main__":
	app.run(debug=True)