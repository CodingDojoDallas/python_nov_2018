from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/play')

def Play():
    return render_template("index.html")

@app.route('/play/<value>')

def Draw(value):
    return render_template("box.html", val = int(value))

@app.route('/play/<value>/<color>')

def Recolor(value, color):
    return render_template("boxcolor.html", val = int(value), col = color)

if __name__ =="__main__":
    app.run(debug=True)