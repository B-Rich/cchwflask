import os
from flask import Flask
from provisional import Provisional, register_app

app = Flask(__name__)

class HelloWorld(Provisional):

    @app.route('/')
    def hello(self):
        return "hello"

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
