from project import app
from flask import render_template, redirect, url_for

@app.route('/', methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def home():
    return render_template('Home.html', title = 'Home')

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('Login.html', title = 'Login')

@app.route('/logout', methods=['POST','GET'])
def logout():
    return redirect('login')