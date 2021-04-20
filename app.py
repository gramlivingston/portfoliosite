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
        

@app.route('/', methods = ['GET'])
def index():

    if request.method == 'GET':
        prjt = 'About'
        return render_template('index.html', project=prjt)

 

@app.route('/projects/<title>')
def projects(title):
    title = request.args['title']
    #child = title
    imgnum = 2
    print(f'project{title}')
    return render_template('projects.html', project=title)