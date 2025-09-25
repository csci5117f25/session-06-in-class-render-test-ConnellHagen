from flask import Flask, redirect, render_template, request
from database import *

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    guests = get_guests()
    return render_template('hello.html', name=name, guests=guests)

@app.post('/submitForm')
def submit():
    text = request.form.get('guest')
    save_guest(text)
    return redirect('/')
