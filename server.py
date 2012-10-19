import os
from flask import Flask, url_for
from provisional import Provisional, register_app

app = Flask(__name__)

methods = ['create', 'update', 'delete', 'health_check']

class HelloWorld(Provisional):

    @app.route('/')
    def print_links():
        links = []
        for m in methods:
            links.append("<a href='%s'>%s</a>" % (url_for(m), m))
        return "</br>".join(links)

    # Implementations of the provisional methods
    def create(self):
        return "create from user_class"

    def update(self):
        return "update from user_class"

    def delete(self):
        return "delete from user_class"

    def health_check(self):
        return "Health check from user_class"


register_app(app, HelloWorld)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
