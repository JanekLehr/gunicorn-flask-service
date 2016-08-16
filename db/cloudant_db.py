from requests import HTTPError
from cloudant.client import Cloudant

client = None
CLOUDANT_AUTH_FAIL_CODES = [401, 403]


def login(f):
    """
    Decorator to re-login upon 401 or 403 credentials_expired error.
    """
    def func(self, *args, **kw):
        try:
            return f(self, *args, **kw)
        except HTTPError as ex:
            status_code = ex.response.status_code
            if status_code in CLOUDANT_AUTH_FAIL_CODES:
                # Re-login and retry.
                print("Status code is %d, refreshing the Cloudant connection" %
                      status_code)
                self.connect(self.username, self.password)
                return f(self, *args, **kw)
        except:
            raise

    return func


class CloudantDB:
    def __init__(self, db_name, username=None,
                 password=None):
        if client is None:
            self.connect(username, password)
        self.username = username
        self.password = password
        self.db = client[db_name]

    @staticmethod
    def connect(username, password):
        global client
        print("Connecting to client")
        client = Cloudant(username, password, account=username)
        client.connect()

    @staticmethod
    def disconnect():
        global client
        print("Deleting session")
        client.disconnect()
        client = None
