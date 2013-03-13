'''
Website data object and class module

@version: 0.1.1
'''

from google.appengine.ext import db

from apenads.objects import AObject

class OSite(db.Model):
    
    id = db.IntegerProperty()
    
    name = db.StringProperty()
    
    url = db.LinkProperty()
    
    enabled = db.BooleanProperty()
    
    
class ASite(AObject):
    
    data = None
    
    def __init__(self):
        
        self.data = OSite()