

from flask import Flask, render_template, request, redirect, session 
import re
import sendgrid
from flask_db2 import DB2
import ibm_db
import ibm_db_dbi
import os


app = Flask(__name__)

app.secret_key = 'a'

app.config['database'] = 'bludb'
app.config['hostname'] = 'b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud'
app.config['port'] = '31249'
app.config['protocol'] = 'tcpip'
app.config['uid'] = 'xgl34124'
app.config['pwd'] = 'lkP1B5zjTXYPKZUK'
app.config['security'] = 'SSL'
try:
    mysql = DB2(app)

    conn_str='database=bludb;hostname=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;port=31249;protocol=tcpip;\
            uid=xgl34124;pwd=lkP1B5zjTXYPKZUK;security=SSL'
    ibm_db_conn = ibm_db.connect(conn_str,'','')
        
    print("Database connected without any error !!")
except:
    print("IBM DB Connection error   :     " + DB2.conn_errormsg()) 

#HOME--PAGE
@app.route("/home")
def home():
    return render_template("welcomepage.html")
@app.route("/")
def add():
    return render_template("dashboard.html")

#SIGN--UP--OR--REGISTER

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == "POST":
        user_name = request.form['username']
        email = request.form['email']
        pass_word = request.form['password']
        query = "INSERT INTO Admin (username,email,password) values (?,?,?)"
        insert_stmt = ibm_db.prepare(ibm_db_conn, query)
        ibm_db.bind_param(insert_stmt, 1, user_name)
        ibm_db.bind_param(insert_stmt, 2, email)
        ibm_db.bind_param(insert_stmt, 3, pass_word)
        ibm_db.execute(insert_stmt)
        msg = 'Account Created Successfully'
        return render_template("signup.html", msg=msg)

@app.route("/signin",methods=['post','get'])
def signin():
    if request.method=="post":
        return render_template("login.html")
    return render_template("login.html")

@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        
        sql = "SELECT * FROM Admin WHERE username = ? and password = ?"
        stmt = ibm_db.prepare(ibm_db_conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, password)
        result = ibm_db.execute(stmt)
        print(result)
        account = ibm_db.fetch_row(stmt)
        print(account)
        
        param = "SELECT * FROM Admin WHERE username = " + "\'" + username + "\'" + " and password = " + "\'" + password + "\'"
        res = ibm_db.exec_immediate(ibm_db_conn, param)
        dictionary = ibm_db.fetch_assoc(res)


        if account:
            session['loggedin'] = True
            session['id'] = dictionary["ID"]
            userid = dictionary["ID"]
            session['username'] = dictionary["USERNAME"]
            session['email'] = dictionary["EMAIL"]
           
            return redirect('/home')
        else:
            msg = 'Incorrect username / password !'
        
    return render_template('login.html', msg = msg)

app.run(debug=True) 
