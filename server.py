import os
from flask import Flask, url_for
from provisional import Provisional, register_app

app = Flask(__name__)

class HelloWorld(Provisional):

    @classmethod
    def hello(self):
        return "hello"

    def health_check(self):
        return "Health check from user_class"


app.add_url_rule('/', 'hello', HelloWorld.hello)
register_app(app, HelloWorld)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
