import multiprocessing
import gunicorn.app.base
from gunicorn.six import iteritems
import eventlet

from flask_app import app

# Patch system modules to make them friendly to green threads
eventlet.monkey_patch()


class GunicornServer(gunicorn.app.base.BaseApplication):

    def init(self, parser, opts, args):
        pass

    def __init__(self, options=None, port=8080, ):
        default_options = {
            'bind': '%s:%s' % ('0.0.0.0', str(port)),
            'workers': GunicornServer.get_number_of_workers(),
            'worker_class': 'sync',
            'worker_connections': 1000
        }
        if type(options) is dict:
            default_options.update(options)
        self.options = default_options
        self.application = app
        super(GunicornServer, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

    @staticmethod
    def get_number_of_workers():
        return (multiprocessing.cpu_count() * 2) + 1
