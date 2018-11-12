from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("untitled-6.html")
@app.route('/result', methods=['POST'])
def DJresults():
    print("It's coming in")
    print(request.form)
    return render_template("untitled-7.html")

@app.route('/danger')
def danger():
    print("a user tried to visit /danger. we have moved their shit back to the normal page")
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 
