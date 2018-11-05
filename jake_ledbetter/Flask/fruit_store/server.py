from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key="Secret"

@app.route('/')         
def index():
	if "straw" not in session:
		session["straw"]=0
	if "rasp" not in session:
		session["rasp"]=0
	if "apple" not in session:
		session["apple"]=0
	if "black" not in session:
		session["black"] = 0
	return render_template("index.html", straw=session["straw"])

@app.route('/checkout', methods=['POST'])         
def checkout():

	##strawberry
	if request.form['strawberry'] == "0":
		session["straw"] = 0
	if request.form['strawberry'] == "1":
		session["straw"] = 1
	if request.form['strawberry'] == "2":
		session["straw"] = 2
	if request.form['strawberry'] == "3":
		session["straw"] = 3
	if request.form['strawberry'] == "4":
		session["straw"] = 4

		##raspberries
	if request.form['raspberry'] == "0":
		session["rasp"] = 0
	if request.form['raspberry'] == "1":
		session["rasp"] = 1
	if request.form['raspberry'] == "2":
		session["rasp"] = 2
	if request.form['raspberry'] == "3":
		session["rasp"] = 3
	if request.form['raspberry'] == "4":
		session["rasp"] = 4

		##apples
	if request.form['apple'] == "0":
		session["apple"] = 0
	if request.form['apple'] == "1":
		session["apple"] = 1
	if request.form['apple'] == "2":
		session["apple"] = 2
	if request.form['apple'] == "3":
		session["apple"] = 3
	if request.form['apple'] == "4":
		session["apple"] = 4


		##blackberry
	if request.form['blackberry'] == "0":
		session["black"] = 0
	if request.form['blackberry'] == "1":
		session["black"] = 1
	if request.form['blackberry'] == "2":
		session["black"] = 2
	if request.form['blackberry'] == "3":
		session["black"] = 3
	if request.form['blackberry'] == "4":
		session["black"] = 4


	return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html",straws = session["straw"],rasps = session["rasp"], apple = session["apple"], black = session["black"])

if __name__=="__main__":   
    app.run(debug=True)    