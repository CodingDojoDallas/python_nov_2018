from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"



print(__name__)


@app.route("/")
def Index():
    return render_template('dojo_survey.html')


@app.route("/process", methods=["POST"])
def createUserResult():
        if len(request.form["name"]) < 1:
        flash("Name cannot be empty!")

    if len(request.form["comment"]) < 1:
        flash("Comments cannot be empty")

    if len(request.form["comment"]) > 120:
        flash("A comment cannot have more than 120 characters")

    if "_flashes" in session.keys():
        return redirect("/")

    else:
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
    return render_template("result.html")

@app.route("/results", methods =['POST'])
def Results():
    return render_template('dojo_survey_results.html')


@app.route('/danger')
def Danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)