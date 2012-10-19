from flask.views import View

class Provisional(View):

    def _health_check(self):
        # do cc specific creation
        return self.health_check()

    def health_check(self):
        # is abstract
        return "Health check from Provisional"


    def dispatch_request(self):
        # here somehow get whats is in it
        return self.health_check()

def register_app(app, class_):
    app.add_url_rule('/health-check', view_func=class_.as_view('health_check'))
