from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def helloWorld():
    return render_template('0-index.html')
