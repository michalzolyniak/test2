# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:59:48 2020

@author: michal-zolyniak
"""

from flask import Flask,render_template,request, url_for, redirect,jsonify
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
constr = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\michal-zolyniak\Desktop\Local_stuff\Python\Flask\PasValueInLink\Project\Macro_Database.accdb;'

def funQsTrans(i):
    switcher={
          'very satisfied':5,
          'satisfied':4,
          'somewhat dissatisfied':3,
          'dissatisfied':2,
          'very dissatisfied':1,
          }
    return switcher.get(i,"Invalid value")


def funFeedbackExist(id):
    conn = pyodbc.connect(constr)
    cursor = conn.cursor()   
    sql_select = "select * from tblFeedback WHERE MacroID= %s" % (id)
    cursor.execute(sql_select)
    records = cursor.fetchall()
    for row in records:
        feedAdded = row.UpdatedFeedbackQuestions
    return feedAdded 
    cursor.close()
    conn.close() 

def funAddFeedback(id,q1,q2,q3,q4,q5,q6): 
    conn = pyodbc.connect(constr)
    cursor = conn.cursor()
    sql_update = "UPDATE tblFeedback SET q1=%s,q2=%s,q3='%s',q4=%s,q5=%s,q6=%s,UpdatedFeedbackQuestions=%s WHERE MacroID= %s" % (q1,q2,q3,q4,q5,q6,1,id)
    cursor.execute(sql_update)                          
    conn.commit()
    cursor.close()
    conn.close() 


@app.route('/main', methods=['GET', 'POST'])
def main():
    idMacro =request.args.get('id')
    if request.method == 'POST':
        q1 = funQsTrans(request.form['q1'])
        q2 = funQsTrans(request.form['q2'])   
        q3 = request.form['AddText']
        q4 = funQsTrans(request.form['q3'])   
        q5 = funQsTrans(request.form['q4'])   
        q6 = funQsTrans(request.form['q5'])        
        funAddFeedback(idMacro,q1,q2,q3,q4,q5,q6)
        return render_template('FeedAdded.html')
    else:
        if funFeedbackExist(idMacro) ==True:
           return render_template('FeedExist.html') 
        else:
           return render_template('Feedback.html')
       

if  __name__=='__main__':
    app.run(debug = False,host='127.0.0.1', port=5000)
    




