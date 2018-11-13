from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template('index.html', times=3)

@app.route('/play/<x>')
def level2(x):
    return render_template('index.html', times = int(x))

@app.route('/play/<x>/<color>')
def level3(x, color):
    return render_template('index.html', times = int(x), color=color)


if __name__ == '__main__':
    app.run(debug=True)