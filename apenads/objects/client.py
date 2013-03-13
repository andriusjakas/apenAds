'''
Created on Mar 13, 2013

@author: andrius
'''

from google.appengine.ext import db
from apenads.objects.user import OUser
from apenads.objects import AObject

class OClient(db.Model):
    id = db.IntegerProperty()
    name = db.StringProperty()
    email = db.EmailProperty()
    user = db.ReferenceProperty(OUser)
    enabled = db.BooleanProperty()
    
class AClient(AObject):
    
    data = None
    
    def __init__(self):
        
        self.data = OClient()