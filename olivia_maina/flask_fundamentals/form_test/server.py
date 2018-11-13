from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # we'll talk about the following two lines after we learn a little more about forms
    name = request.form['first_name']
    email = request.form['email']
    # redirects back to the '/' route
    return render_template('create.html')


@app.route('/show')
def show_user():
    return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')


if __name__ == "__main__":
    app.run(debug=True)
