# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from MagicMirror import app
from Apilib import Rapi
#from flask import *
from flask.globals import request

@app.route('/',methods=['GET',"POST"])
def home():
    return render_template(
        'index.html',
        title="Magic Mirror",
        button="Send",
        year=datetime.now().year,
    )
@app.route('/roobot',methods=['GET','POST'])
def roobot():
    if request.method == "POST":
        message=request.form['message']
        try:
            Answer=Rapi.Roobot(message)
        except Exception:
            Answer=""
        return Answer
    else:
        return "<p>No Message<p>"
    
@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
