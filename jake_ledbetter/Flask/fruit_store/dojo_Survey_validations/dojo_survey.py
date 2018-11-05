from flask import Flask, render_template, session, request, redirect, flash
app = Flask (__name__)
app.secret_key="secret"
@app.route('/')
def survey():
	return render_template('dojo_survey.html')

@app.route('/users', methods=['POST'])
def create():
	print(request.form)
	if len(request.form["name"]) < 1:
		flash("Name cant be blank")
		return redirect('/')
	if (len(request.form['comment']) > 120):
		flash("Comment is too long")
		return redirect('/')
	if(len(request.form['comment'])<1):
		flash("Comment cant be empty")
		return redirect('/')
	print('Name', request.form['name'])
	print("Location ", request.form['location'])
	print("Language ", request.form['language'])
	return render_template("created.html")
@app.route('/danger')
def danger():
	print("a user tried to visit/danger/we have redirected the user to /")
	return redirect("/")

if __name__ == ('__main__'):
	app.run(debug=True)