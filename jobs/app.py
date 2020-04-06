import sqlite3

from flask import Flask, render_template, g
PATH = 'db/jobs.sqlite'
app = Flask(__name__)
def open_connection():
    connection = getattr(g,'_connection',None)
     if Connection = None:
         Connection = g._connection = sqlite3.connect(PATH)
    Connection.row_factory = sqlite3.Row
    return Connection

def execute_sql(sql, values=(), commit=False, single=False):
    Connection = open_connection()
    cursor=connection.execute(sql,values)
    if commit=true:
        results= connection.commit()
    else:
        results= cursor.fetchone() if single else curso.fetchall()
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()
    curso.close()
    return results
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
