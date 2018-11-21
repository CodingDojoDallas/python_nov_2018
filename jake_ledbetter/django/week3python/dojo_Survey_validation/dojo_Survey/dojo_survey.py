from flask import Flask, render_template, session, request, redirect
app = Flask (__name__)

@app.route('/')
def survey():
	return render_template('dojo_survey.html')

@app.route('/users', methods=['POST'])
def create():
	print(request.form)
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