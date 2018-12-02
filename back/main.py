#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for, make_response
from flask_restful import Resource, Api
from pprint import pprint as pp
import json

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=['GET', 'POST'])
def index():
	return make_response(open('templates/welcome.html').read())

class Builder(Resource):
    def get(self):
        return make_response(open('templates/layout.html').read())

api.add_resource(Builder, '/builder') # Route_1


if __name__=='__main__':
    app.run(debug=True)
