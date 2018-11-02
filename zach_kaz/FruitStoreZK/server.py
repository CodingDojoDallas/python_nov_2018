from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    apples=int(request.form['apple'])
    raspberries=int(request.form['raspberry'])
    blackberries=int(request.form['blackberry'])
    strawberries=int(request.form['strawberry'])
    numitems=apples+raspberries+blackberries+strawberries
    print(apples, raspberries,blackberries,strawberries,numitems)
    now=datetime.now().strftime('%c')
    return render_template('checkout.html',now=now,x=numitems,a=apples,r=raspberries,b=blackberries,s=strawberries)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    