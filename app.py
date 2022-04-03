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


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        print("Post method ")
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
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
                      "Subject": subject,
                      "TextPart": "Name - "+name+"\nEmail - "+email+"\n"+message,
                      "CustomID": "AppGettingStartedTest"
                    }
                  ]
                }
        
        result = mailjet.send.create(data=data)
        print(result)
        flash("Email Successfully sent")
        return redirect(url_for('index'))

    return render_template('index.html')





if __name__ == '__main__':
	app.run(debug=True)
