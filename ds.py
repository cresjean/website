__author__ = 'crespo'
from google.appengine.ext import ndb

class Code(ndb.Model):
    lines = ndb.IntegerProperty()
    commits = ndb.IntegerProperty()
    pr = ndb.IntegerProperty()
    updated_time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_one(cls):
        return cls.query().get()
