from flask.views import View


class InternalProvisional(View):

    # initialisation for routing requests
    def __init__(self, func):
        self.func = func

    # hidden methods
    def _create(self):
        return self.create()

    def _update(self):
        return self.update()

    def _delete(self):
        return self.delete()

    def _health_check(self):
        return self.health_check()

    def dispatch_request(self):
        if self.func == 'create':
            return self._create()
        elif self.func == 'update':
            return self._update()
        elif self.func == 'delete':
            return self._delete()
        elif self.func == 'health_check':
            return self._health_check()


class Provisional(InternalProvisional):
    """ Base class for Provisional
    Notes
    -----
    To work successfully, 'class_' must implement 'create', 'update', 'delete'
    and 'health_check'.
    """
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
    app.add_url_rule('/update',
            view_func=class_.as_view('update',
            func='update'))
    app.add_url_rule('/delete',
            view_func=class_.as_view('delete',
            func='delete'))
    app.add_url_rule('/health-check',
            view_func=class_.as_view('health_check',
            func='health_check'))
