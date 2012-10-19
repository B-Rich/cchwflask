from flask.views import View

class InternalProvisional(View):
    """ CC specific scaffolding class. """

    # initialisation for routing requests
    def __init__(self, func, data=None):
        self.func = func

    # hidden methods
    def _create(self, data):
        return self.create(data)

    def _update(self, data):
        return self.update(data)

    def _delete(self, data):
        return self.delete(data)

    def _health_check(self):
        return self.health_check()

    def dispatch_request(self, data=None):
        if data is not None:
            # decode json
            pass
        if self.func == 'create':
            return self._create(data)
        elif self.func == 'update':
            return self._update(data)
        elif self.func == 'delete':
            return self._delete(data)
        elif self.func == 'health_check':
            return self._health_check()


class Provisional(InternalProvisional):
    """ Base class for Provisional.  """

    # methods to be implemented by user
    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def health_check(self):
        pass

def register_app(app, class_):
    """ Registration of provisional handler.

    Parameters
    ----------
    all : flask app
        your flask app
    class_ : class
        the provisional handler

    """
    app.add_url_rule('/create/<data>',
            view_func=class_.as_view('create',
            func='create'))
    app.add_url_rule('/update/<data>',
            view_func=class_.as_view('update',
            func='update'))
    app.add_url_rule('/delete/<data>',
            view_func=class_.as_view('delete',
            func='delete'))
    app.add_url_rule('/health-check',
            view_func=class_.as_view('health_check',
            func='health_check'))
