# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from Apilib import Rapi
from flask import *
from MagicMirror import app
from flask.globals import request

@app.route('/',methods=['GET',"POST"])
def home():
    return render_template(
        'index.tpl',
        title="Magic Mirror",
        button="Send",
        year=datetime.now(),
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
    
@app.route('/study',methods=['GET','POST'])
def study():
    if request.method == "POST":
        message=request.form['message']
        try:
            Answer=Rapi.Roobot(message)
        except Exception:
            Answer=""
        return Answer
    else:
        return render_template(
        'study.tpl',
        title='Methion learning',
        year=datetime.now(),
        message=''
        )
    
@app.route('/about')
def about():
    return render_template(
        'about.tpl',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
