from flask import Flask, url_for, flash, render_template, redirect, request, g, send_from_directory
from flask import session as login_session
from model import *
from werkzeug.utils import secure_filename
import locale, os
app=Flask(__name__)

def verify_password(username, password):
	user=session.query(Users).filter_by(name=username).first()
	if not user or not user.verify_password(password):
		return False
	g.user = user
	return True

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	elif request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		if username is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for('login'))
		if verify_password(username, password):
			user=session.query(Users).filter_by(name=username).one()
			flash('Login Successful, welcome, %s' % user.name)
			login_session['user']=user.name
			login_session['id']=user.id
			return redirect(url_for(''))
		else:
			flash('Incorrect username/password combination')
			return redirect(url_for('login'))

#@app.route('/setting', methods=['GET', 'POST'])
#def change_username():
#	if request.method=='GET':
#		return render_template('setting.html')
	


if __name__=='__main__':
	app.run()