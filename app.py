#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:09:56 2021

@author: ashish
"""


from flask import Flask, render_template,request,redirect,url_for,flash
from mailjet_rest import Client


api_key = '63588ea5f6af7e6be84944a685f80152'
api_secret = 'e23d5310dde40c1a934aff632c469057'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')



#data = code_generator.generate()

app = Flask(__name__)
app.config['SECRET_KEY']='Website'



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
        data = {
                  'Messages': [
                    {
                      "From": {
                        "Email": "ashm.jagadeesh@gmail.com",
                        "Name": name
                      },
                      "To": [
                        {
                          "Email": "ashm.jagadeesh@gmail.com",
                          "Name": "Ashish M J"
                        }
                      ],
                      "Subject": "Mail From Website",
                      "TextPart": "Name - "+name+"\nEmail - "+email+"\n"+msg,
                      "CustomID": "AppGettingStartedTest"
                    }
                  ]
                }
        
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print("Mail Sent")
        flash("Email Successfully sent. ")
        return redirect(url_for('contact'))
    return render_template('contact.html')



if __name__ == '__main__':
	app.run(debug=True)