from flask import Flask, render_template, redirect, request
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    total = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    x = datetime.datetime.now().strftime("%c")
    name = request.form['name']
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    studentid = request.form['studentid']
    return render_template('checkout.html', total=total, date=x)

if __name__ == '__main__':
    app.run(debug=True)