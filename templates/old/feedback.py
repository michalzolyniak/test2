# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:59:48 2020

@author: michal-zolyniak
"""

from flask import Flask,render_template,request, url_for, redirect,jsonify
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\michal-zolyniak\Desktop\Local_stuff\Python\Flask\PasValueInLink\feedback.accdb;')


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST': 
        i = request.form["fname"]
        print(i)
        return redirect(url_for('feedback.html'))
    return render_template('feedback.html')


@app.route('/AddFeedbackDatabase',methods=['GET', 'POST'])
def AddFeedbackDatabase():
    title = request.args.get('title')   
    startdate = request.args.get('startdate')
    print(title)
    print(startdate)
    cursor = conn.cursor()
    sql_update = "UPDATE feedback SET startdate='%s' WHERE title='%s'" % (startdate, title)
    cursor.execute(sql_update)                          
    conn.commit()
    return jsonify({'tableLog':'test'})
if  __name__=='__main__':
    app.run(debug = False,host='127.0.0.1', port=5000)
    
    
#[x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
    # cursor.execute('''
    #                 INSERT INTO feedback (title, startdate)
    #                 VALUES('Mike', 'Jordan')

    #               ''')
  # test = 'mz'
    # sql_update = "UPDATE feedback SET title='%s', startdate='%s' WHERE title='%s'" % (title, startdate, test)                                    
  
