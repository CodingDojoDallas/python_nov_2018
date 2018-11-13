from flask import Flask, render_template, request, redirect, url_for, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def createUserResult():
    if len(request.form["email"]) < 1:
        flash("Email cannot be empty!")

    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email Address!")

    if len(request.form["first_name"]) < 1:
        flash("First name cannot be empty")

    elif not request.form["first_name"].isalpha():
        flash("First name can contain only letters!")

    if len(request.form["last_name"]) < 1:
        flash("Last name cannot be empty")

    elif not request.form["first_name"].isalpha():
        flash("Last name can contain only letters!")

    if len(request.form["password1"]) < 1:
        flash("Password cannot be empty")

    elif len(request.form["password1"]) < 8:
        flash("Password needs to be more than 8 characters")

    if len(request.form["password2"]) < 1:
        flash("Confirm password cannot be empty")

    elif request.form["password1"] != request.form["password2"]:
        flash("Password and Passworkd Confirmation DO NOT MATCH!")

    if "_flashes" in session.keys():
        return redirect("/")

    else:
        return "All Good!"

    return render_template("result.html")

@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/danger")
def danger():
    print("a user tried to vist /danger")
    return redirect(url_for("/"))








if __name__=="__main__":
    app.run(debug=True)
