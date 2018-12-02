from flask import Flask, flash, redirect, render_template, request, url_for
from pprint import pprint as pp
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('welcome.html')

@app.route('/builder', methods=['GET', 'POST'])
def builder():
    return render_template('builder.html')


if __name__=='__main__':
    app.run(debug=True)
