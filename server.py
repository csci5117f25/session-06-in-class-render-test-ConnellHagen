from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.post('/submitForm')
def submit():
    text = request.args.get('thebox')
    print(request.args)
    return render_template('hello.html')
