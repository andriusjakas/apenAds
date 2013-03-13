'''
Banner position data object and class

@version: 0.1.1
'''
from google.appengine.ext import db
from apenads.objects import OSite
from apenads.objects import AObject

class OZone(db.Model):
    
    id = db.IntegerProperty()
    
    name = db.StringProperty()
    
    site = db.ReferenceProperty(OSite)
    
    enabled = db.BooleanProperty()
    
    
class AZone(AObject):
    
    data = None
    
    def __init__(self):
        
        self.data = OZone()
    