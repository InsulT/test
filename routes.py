from flask import Flask, render_template
from flask import views
from flask import flash
from flask import request
import time
import datetime
from time import gmtime, strftime
import os
import json
app = Flask(__name__)
app.secret_key = "asasdasdad"

@app.route('/')
def home():
    return render_template("home.html",)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/test/', methods=['POST', 'GET'])
def test():
    dict = {}
    if request.method == 'POST' and 'ido' in request.form:
        time = datetime.datetime.now() + datetime.timedelta(hours=1)
        flash(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'ido')
        render_template('test.html')
    elif request.method == 'POST' and 'exp' in request.form:
        #result = eval(request.form['exp'])
        result1 = request.form['exp']
        flash(result1, 'kiir')
        return render_template("test.html")
    elif request.method == 'POST' and 'leker' in request.form:
        f = open('gamelist.json','r')
        dict = json.load(f)
    return render_template("test.html", dicts=dict)


if __name__ == '__main__':
    app.debug = True
    app.run()
