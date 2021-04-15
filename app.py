#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:09:56 2021

@author: ashish
"""


from flask import Flask, render_template
from flask_mail import Message,Mail


app = Flask(__name__)
app.config['SECRET_KEY']='Website'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=""
app.config['MAIL_PASSWORD']=""
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True



@app.route('/')
def home():
    return render_template('template.html')


if __name__ == '__main__':
	app.run(debug=True)