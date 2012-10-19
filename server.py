import os
from flask import Flask, url_for
from provisional import Provisional

app = Flask("HelloWorld")

methods = ['create', 'update', 'delete', 'health_check']

@app.route('/')
def hello():
    links = []
    for m in methods:
        links.append("<a href='%s'>%s</a>" % (url_for(m), m))
    return "</br>".join(links)

@app.route('/create')
def create():
    return "created"

@app.route('/update')
def update():
    return "updated"

@app.route('/delete')
def delete():
    return "deleted"

@app.route('/health-check')
def health_check():
    return "All your cloud are belong to us!"

app.register_blueprint(Provisional)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
