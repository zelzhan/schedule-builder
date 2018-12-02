from flask import Flask, flash, redirect, render_template, request, url_for
from pprint import pprint as pp
import json
from buttons import Button

data = [[' BIOL 101', 'Biology for non-Science majors', '2L', '3.0', '6', 'MWF', '04:00 PM-04:50 PM', '33', '48', 'Zhanat Muminova', '7.105 - cap:80'],
        [' BIOL 101', 'Biology for non-Science majors', '1L', '3.0', '6', 'MWF', '02:00-PM-02:50 PM', '48','48', 'Anara Zhumadilova', '7E529 - cap:105'],
		[' BIOL 110', 'Modern Biology I with Lab',     '1BLb', '4.0', '8', 'T',  '03:00 PM-05:50 PM', '3', '24', 'Ferdinand Molnar', '9.228 - cap:40'],
		[' BIOL 110', 'Modern Biology I with Lab',      '1L', '4.0', '8', 'TR',  '12:00 PM-01:15 PM', '3', '24', 'Ferdinand Molnar', '7.427 - cap:26'],
		[' BIOL 120', 'Modern Biology II with Lab',    '1BLb', '4.0', '8', 'M',  '12:00 PM-02:50 PM',  '24', '24','Zhalgas Serimbetov', '9.228 - cap:40'],
		[' BIOL 120', 'Modern Biology II with Lab',    '3BLb', '4.0', '8', 'W',  '12:00 PM-02:50 PM',  '23','24', 'Zarina Sautbayeva',  '9.228 - cap:40'],
		[' BIOL 120', 'Modern Biology II with Lab',    '4BLb', '4.0', '8', 'W',  '03:00 PM-05:50 PM', '24','24', 'Zarina Sautbayeva',  '9.228 - cap:40'],
		[' BIOL 120', 'Modern Biology II with Lab', '5BLb', '4.0', '8', 'F',     '12:00 PM-02:50 PM', '24','20','Zhalgas Serimbetov', '9.228 - cap:40'],
		[' BIOL 120', 'Modern Biology II with Lab', '2BLb', '4.0', '8', 'W',     '03:00 PM-05:50 PM',  '24','24','Zhalgas Serimbetov', '7.407 - cap:20'],
		[' BIOL 120', 'Modern Biology II with Lab', '1L', '4.0', '8', 'TR',      '03:00 PM-04:15 PM', '72','72', 'Anna Andreeva','7E.329 - cap:104'],
		[' BIOL 120', 'Modern Biology II with Lab', '2L', '4.0', '8', 'TR',      '04:30 PM-05:45 PM', '43', '72','Anna Andreeva','7E.529 - cap:104'],
		[' BIOL 231', 'Human Anatomy and Physiology II', '1BLb', '4.0', '8', 'M','03:00 PM-05:50 PM', '24','24','Tursonjan Tokay', '7E.217 - cap:24'],
		[' BIOL 231', 'Human Anatomy and Physiology II', '2BLb', '4.0', '8', 'T','03:00 PM-05:50 PM', '24','24','Tursonjan Tokay', '7E.217 - cap:24'],
		[' BIOL 231', 'Human Anatomy and Physiology II', '3BLb', '4.0', '8', 'W', '03:00 PM-05:50 PM', '24', '24', 'Anara Zhumadilova', '7E.217 - cap:24']]

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=['GET', 'POST'])
def index():
	send = Button()
	if send.validate_on_submit():
		return redirect(url_for('builder'))
	return render_template('welcome.html', form = send)

@app.route('/builder', methods=['GET', 'POST'])
def builder():
    return render_template('builder.html', data=data)





if __name__=='__main__':
    app.run(debug=True)
