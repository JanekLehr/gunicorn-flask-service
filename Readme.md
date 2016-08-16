# Gunicorn Flask Service

Standalone application running with gunicorn and flask. This is meant as more of a template to create more fleshed out applications. 
It comes with a skeleton for interacting with a Cloudant database.

This implementation uses an eventlet worker instead of the default synchronous worker, but others can be substituted in. 
See the [Gunicorn settings](http://docs.gunicorn.org/en/stable/settings.html) for more information.
