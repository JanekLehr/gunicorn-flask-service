from engine.gunicorn_server import GunicornServer

if __name__ == '__main__':
    server = GunicornServer(options={
        'worker_class': 'eventlet'
    })
    server.run()
