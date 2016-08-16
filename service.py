import eventlet
# Patch system modules to make them friendly to green threads
eventlet.monkey_patch()

from engine.gunicorn_server import GunicornServer  # noqa

if __name__ == '__main__':
    server = GunicornServer(options={
        'worker_class': 'eventlet'
    })
    server.run()
