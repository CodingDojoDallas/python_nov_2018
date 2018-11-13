from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

print(__name__)
@app.route("/")
def Index():
    return render_template('dojo_survey.html')

@app.route("/results", methods =['POST'])
def Results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('dojo_survey_results.html')

@app.route('/home', methods = ['POST'])
def Home():
    return redirect('/')

@app.route('/danger')
def Danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)