from flask import Flask, render_template
app = Flask(__name__)

print(__name__)
@app.route('/')
def Index():
    users = (
    {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name': 'Michael Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name': 'John Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name': 'Mark Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name': 'KB Tonel'}
    );    
    header = []
    for key in users[0].keys():
        header.append(str(key))
        print(header)


    return render_template('table.html', users = users, len = (len(users) + 1), header = header)



if __name__=="__main__":
    app.run(debug=True)  