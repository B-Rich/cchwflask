from flask.views import View

class Provisional(View):

    def dispatch_request(self):
        return "Health check from Provisional"

def register_app(app, class_):
    app.add_url_rule('/health-check', view_func=class_.as_view('health_check'))
