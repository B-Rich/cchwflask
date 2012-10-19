import os
from flask import Flask, url_for
from provisional import Provisional, register_app

app = Flask(__name__)

methods = ['create', 'update/id_', 'delete/id_', 'health_check']

class ProvisionalExample(Provisional):

    @app.route('/')
    def print_links():
        ans = """
<form action="create" method="post">
  <input type="text" name="data" value="some_json_data" />
  <input type="submit" value='post -> create!' />
</form>
<form action="update/coffee" method="put">
  <input type="text" name="data" value="some_json_data" />
  <input type="submit" value='put -> update!' />
</form>
<a href='delete/coffee'> delete -> delete/coffee</a> </br>
<a href='health_check'> health_check -> health_check</a>
    """
        return ans

    # Implementations of the provisional methods
    def create(self, data):
        return "create from user_class, data: '%s'" % data

    def update(self, id_, data):
        return "update from user_class, id_: %s data: '%s'" % (id_, data)

    def delete(self, id_):
        return "delete from user_class, id_: '%s'" % id_

    def health_check(self):
        return "Health check from user_class"


register_app(app, ProvisionalExample)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
