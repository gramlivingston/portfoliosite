from flask import Flask, request, redirect, url_for, render_template
import json
import requests

app = Flask(__name__)


@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)
        

@app.route('/')
def index():
    if flask.request.method == 'POST':
        username = flask.request.values.get('bttnlink')
        print(username)
        return render_template('index.html', prjt=username)
    else:
    return render_template('index.html')


@app.route('/project')
def project():
    cp = (request.args.get('value'))
    print(cp)
    return render_template('index.html', prjt=cp)