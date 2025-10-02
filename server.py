from flask import Flask, redirect, render_template, request, session
from database import *

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET']

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    guests = get_guests()
    return render_template('hello.html', name=name, guests=guests)

@app.route('/grail')
def grail():
    return render_template('grail.html')

@app.post('/submitForm')
def submit():
    text = request.form.get('guest')
    save_guest(text)
    return redirect('/')
