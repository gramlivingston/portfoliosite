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
        

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        prjt = request.form['btnlink']
        return render_template('projects.html', project=prjt)
    if request.method == 'GET':
        prjt = 'About'
        return render_template('index.html', project=prjt)


@app.route('/projects')
def project():
    prjt = request.form['btnlink']
    print(f'project = {prjt}')
    return render_template('index.html', project=prjt)