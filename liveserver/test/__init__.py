from liveserver.test.testcases import LiveServerTestCase

# ConnectionHandler.__setitem__ is only available in Django 1.4
from django.db.utils import ConnectionHandler
if not hasattr(ConnectionHandler, "__setitem__"):
    def set_item(self, key, value):
        self._connections[key] = value
    
    ConnectionHandler.__setitem__ = set_item

__all__ = ["LiveServerTestCase"]