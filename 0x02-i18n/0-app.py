from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def helloWorld():
    '''Render hello world
    '''
    return render_template('0-index.html')
