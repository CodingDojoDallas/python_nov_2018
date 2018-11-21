from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="Secret"
@app.route('/')
def count():
	if "current_count" not in session:
		session["current_count"] = 0
	if "current_count" in session:
		session["current_count"] += 1
	return render_template("count.html", current_count = session["current_count"])

@app.route("/inc", methods=["POST"])
def incBy2():
	session["current_count"] += 1
	return redirect('/')

@app.route("/reset", methods=["POST"])
def clear():
	session["current_count"] = 0
	return redirect('/')
if __name__ =="__main__":
	app.run(debug=True)
