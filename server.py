# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:05:29 2020

@author: Menios
"""

from flask import Flask, render_template, request
app = Flask(__name__)
print(__name__)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
	
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    
	if request.method == 'POST':
		data = request.form.to_dict()
		print(data)
		return 'form submitted'
	else:
		return 'error'