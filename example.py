import os
from flask import Flask, url_for
from provisional import Provisional, register_app

app = Flask(__name__)

methods = ['create', 'update/id_', 'delete/id_', 'health_check']

class ProvisionalExample(Provisional):

    @app.route('/')
    def print_links():
        links = []
        for m in methods:
            links.append("<a href='%s'>%s</a>" % (m, m))
        return "</br>".join(links)

    # Implementations of the provisional methods
    def create(self, data):
        return "create from user_class, data: '%s'" % data

    def update(self, data):
        return "update from user_class, data: '%s'" % data


    def delete(self, data):
        return "delete from user_class, data: '%s'" % data

    def health_check(self):
        return "Health check from user_class"


register_app(app, ProvisionalExample)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
