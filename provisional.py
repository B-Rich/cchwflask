from flask.views import View, request

class InternalProvisional(View):
    """ CC specific scaffolding class. """

    methods = ['GET', 'POST', 'DELETE', 'PUT']
    # initialisation for routing requests
    def __init__(self, func, data=None):
        self.func = func

    # hidden methods
    def _create(self, data):
        return self.create(data)

    def _update(self, id_, data):
        return self.update(id_, data)

    def _delete(self, id_):
        return self.delete(id_)

    def _health_check(self):
        return self.health_check()

    def dispatch_request(self, id_=None):
        if id_ is not None:
            # decode json
            pass
        if self.func == 'create':
            return self._create(request.values)
        elif self.func == 'update':
            return self._update(id_, request.values)
        elif self.func == 'delete':
            return self._delete(id_)
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
    app.add_url_rule('/create',
            view_func=class_.as_view('create',
            func='create'))
    app.add_url_rule('/update/<id_>',
            view_func=class_.as_view('update',
            func='update'))
    app.add_url_rule('/delete/<id_>',
            view_func=class_.as_view('delete',
            func='delete'))
    app.add_url_rule('/health_check',
            view_func=class_.as_view('health_check',
            func='health_check'))
