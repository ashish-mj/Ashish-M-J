#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:09:56 2021

@author: ashish
"""


from flask import Flask, render_template,request,redirect,url_for,flash
import code_generator
from flask_mail import Message,Mail

data = code_generator.generate()

app = Flask(__name__)
app.config['SECRET_KEY']='Website'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=data[0]
app.config['MAIL_PASSWORD']=data[1]
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')



@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['msg']
        subject="Mail from website"
        info = Message(subject,sender = "ana.customer1000@gmail.com",recipients = ['ashm.jagadeesh@gmail.com'])
        info.body = "Name : " + str(name) + "\nEmail : " + str(email) + '\n'+str(msg)
        mail.send(info)
        print("Mail Sent")
        flash("Email Successfully sent. ")
        return redirect(url_for('contact'))
    return render_template('contact.html')



if __name__ == '__main__':
	app.run(debug=True)