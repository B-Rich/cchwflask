import os
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    print url_for('create')
    print url_for('update')
    print url_for('delete')
    print url_for('health-check')

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
