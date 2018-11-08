from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from datetime import datetime
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key='secretness'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
bcrypt = Bcrypt (app)

@app.route('/')
def start():
    return render_template('walllogin.html')

@app.route('/logoff')
def loggingoff():
    session.clear
    return redirect('/')

@app.route('/wall')
def wallpresent():
    userid=session['user']
    data={
        'userid':userid
    }
    estuser = connectToMySQL("friendsdb")
    currentuser= estuser.query_db("SELECT * FROM `friendsdb`.`logins` WHERE `friendsdb`.`logins`.`id`=%(userid)s",data)
    xyz = connectToMySQL('friendsdb').query_db("SELECT COUNT(`messages`.`id`) FROM `friendsdb`.`messages` WHERE `friendsdb`.`messages`.`senderid`=%(userid)s",data)
    print('########')
    print(xyz)
    nummymsg=xyz[0]['COUNT(`messages`.`id`)']
    getmsg = connectToMySQL('friendsdb')
    userdata={
        'id':currentuser[0]['id']
    }
    msgtouser= getmsg.query_db("SELECT * FROM `friendsdb`.`messages` JOIN `friendsdb`.`logins` ON `messages`.`senderid`=`logins`.`id` WHERE `friendsdb`.`messages`.`idreciever`=%(id)s AND `friendsdb`.`messages`.`read`='unread'",userdata)
    otherusers = connectToMySQL('friendsdb')
    others= otherusers.query_db("SELECT `id`,`first_name`, `last_name` FROM `friendsdb`.`logins` WHERE `friendsdb`.`logins`.`id` !=%(userid)s",data)
    for i in others:
        if 'first_name' not in i:
            i['first_name']='unknown'
        if 'last_name' not in i:
            i['last_name']='unknown'
    return render_template('messagepage.html',otherusers=others,user=currentuser,msgtouser=msgtouser, nummymsg=nummymsg)
@app.route('/sentmsgs')
def seemymsg():
    getmsg = connectToMySQL('friendsdb')
    userid=session['user']
    data={
        'userid':userid
    }
    mymsg= getmsg.query_db("SELECT * FROM `friendsdb`.`messages` JOIN `friendsdb`.`logins` ON `messages`.`idreciever`=`logins`.`id` WHERE `friendsdb`.`messages`.`senderid`=%(userid)s",data)
    return render_template('sentmessagespage.html',mymsg=mymsg)

@app.route('/rcvdmsgs')
def showrcvdmsgs():
    getmsg = connectToMySQL('friendsdb')
    userid=session['user']
    data={
        'userid':userid
    }
    mymsg= getmsg.query_db("SELECT * FROM `friendsdb`.`messages` JOIN `friendsdb`.`logins` ON `messages`.`senderid`=`logins`.`id` WHERE `friendsdb`.`messages`.`idreciever`=%(userid)s",data)
    return render_template('recievedmessagespage.html',mymsg=mymsg)


@app.route('/deletemsg', methods=['post'])
def deletemessage():
    data={
        'messageid':request.form['msgid']
    }
    deleteit=connectToMySQL('friendsdb').query_db("DELETE FROM `friendsdb`.`messages` WHERE `messages`.`id`=%(messageid)s",data)
    return redirect('/sentmsgs')

@app.route('/markreadwall', methods=['post'])
def markreadwall():
    data={
        'messageid':request.form['msgid']
    }
    deleteit=connectToMySQL('friendsdb').query_db("UPDATE `friendsdb`.`messages` SET `read`='read' WHERE `messages`.`id`=%(messageid)s",data)
    return redirect ('/wall')

@app.route('/markreadrcvd', methods=['post'])
def markreadrecvd():
    data={
        'messageid':request.form['msgid']
    }
    deleteit=connectToMySQL('friendsdb').query_db("UPDATE `friendsdb`.`messages` SET `read`='read' WHERE `messages`.`id`=%(messageid)s",data)
    return redirect ('/rcvdmsgs')


@app.route('/sendmessage', methods =['post'])
def sendmsg():
    mysql = connectToMySQL("friendsdb")
    data={
        'sender':session['user'],
        'reciever':request.form['msgreciever'],
        'text':request.form['msgtext'],
        'created_at':datetime.now().strftime('%Y-%m-%d'),
        'updated_at':datetime.now().strftime('%Y-%m-%d')
        }
    msg = mysql.query_db("INSERT INTO `friendsdb`.`messages` (`senderid`,`idreciever`,`read`,`text`,`created_at`,`updated_at`) VALUES (%(sender)s,%(reciever)s,'unread',%(text)s,%(created_at)s,%(updated_at)s)",data)  
    return redirect('/wall')

@app.route('/reg')
def show():
    return render_template('wallregcomplete.html')

@app.route('/logintest', methods=['post'])
def logincheck():
    mysql = connectToMySQL("friendsdb")
    email=request.form['email']
    data= {
        'email':email
    }
    checkstuff= mysql.query_db("SELECT * FROM `friendsdb`.`logins` WHERE `friendsdb`.`logins`.`email`=%(email)s",data)
    if bcrypt.check_password_hash(checkstuff[0]['pwhash'],request.form['pw'])==True:
        session['user']=checkstuff[0]['id']
        return redirect ('/wall')
    else:
        flash("Your password didn't match. Please try again",'login')
        return redirect ('/')

@app.route('/regtest', methods=['post'])
def regtest():
    validreg=True
    if (len(request.form['firstname'])< 2) or (not NAME_REGEX.match(request.form['firstname'])):
        flash("First name must be at least two characters long and only be letters", 'firstname')
        validreg=False
    if (len(request.form['lastname'])< 2) or (not NAME_REGEX.match(request.form['lastname'])):
        flash("Last name must be at least two characters long and only be letters",'lastname')
        validreg=False
    if (len(request.form['email'])< 1) or (not EMAIL_REGEX.match(request.form['email'])):
        flash("Please enter a valid email address",'email')
        validreg=False
    if (len(request.form['pw'])<8):
        flash("Your password must contain at least eight characters",'password')
        validreg=False
    if (request.form['pw']!= request.form['pwconfirm']):
        flash("Your passwords did not match.",'confirmpassword')  
        validreg=False  
    if (validreg== False):
        print('#$##*&^@*$&^#(%)')
        print(flash)
        return redirect('/')
    else:
        mysql = connectToMySQL("friendsdb")
        fn=request.form['firstname']
        ln=request.form['lastname']
        email=request.form['email']
        college=request.form['college']
        time=datetime.now().strftime('%Y-%m-%d')
        hash=bcrypt.generate_password_hash(request.form['pw'])
        data={
            'firstname':fn,
            'lastname':ln,
            'email':email,
            'college':college,
            'password':hash,
            'created_at':time,
            'updated_at':time
        }
        insertit = mysql.query_db("INSERT INTO `friendsdb`.`logins` (`first_name`,`last_name`,`email`,`college`,`pwhash`,`created_at`,`updated_at`) VALUES (%(firstname)s,%(lastname)s,%(email)s,%(college)s,%(password)s,%(created_at)s,%(updated_at)s)",data)  
        mysql = connectToMySQL("friendsdb")
        checkstuff= mysql.query_db("SELECT * FROM `friendsdb`.`logins` WHERE `friendsdb`.`logins`.`email`=%(email)s",data)
        session['user']=checkstuff[0]['id']

        return redirect ('/reg')

if __name__ == "__main__":
    app.run(debug=True)
