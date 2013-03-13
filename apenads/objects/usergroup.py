from google.appengine.ext import db

from apenads.objects import AObject

class OUserGroup(db.Model):
    group_id = db.IntegerProperty()
    group_name = db.StringProperty()

class AUserGroup(AObject):
    
    data = None
    
    def __init__(self, group_id = 0, group_name = 'Administrators'):
        self.data = OUserGroup(key_name = str(group_id))
        self.data.group_id = group_id
        self.data.group_name = group_name

    def save(self):
        self.data.put()

        