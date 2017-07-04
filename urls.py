from flask import render_template, flash, request, redirect, url_for

from config.settings import app, db
from apps.hardware.models import Hardware


@app.route('/')
def index():
	# return '<h1>HI</h1>'
	return render_template('homepage.html')

@app.route('/hardware')
def show_all():
	return render_template('hardware/show_all.html', hardware=Hardware.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
	if request.method == 'POST':
		if not request.form['name'] or not request.form['company'] or not request.form['model']:
			flash('Please enter all the fields', 'error')
		else:
			hardware = Hardware(request.form['name'], request.form['company'],
			request.form['model'], request.form['sn'])
         
			db.session.add(hardware)
			db.session.commit()
			flash('Record was successfully added')
			return redirect(url_for('show_all'))
	return render_template('hardware/new.html')