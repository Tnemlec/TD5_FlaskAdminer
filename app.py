from datetime import datetime

from flask import Flask, render_template, request,redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'myawesomepassword'
app.config['MYSQL_DB'] = 'pythonapp'

mysql = MySQL(app)

@app.route('/', methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        now = datetime.now()
        detail = request.form
        content = detail['post']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO posts(ip, date, content) VALUES('" + str(request.remote_addr) + "','" + str(now) + "','" + content + "');")
        mysql.connection.commit()
        cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html",  data=data)
    