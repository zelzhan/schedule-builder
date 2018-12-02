f#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query
from pprint import pprint as pp
from search import Search
import json	

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
 
@app.route('/', methods=['GET', 'POST'])
def index():
	return "Hello world"


if __name__=='__main__':
    app.run(debug=True)