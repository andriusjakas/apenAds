'''
Created on Mar 12, 2013

@version: 
'''

import hashlib

from google.appengine.ext import db

class OApplication(db.Model):
    '''
    Application object data
    '''
    
    
    app_version = db.StringProperty()
    '''
    
    '''
    
    app_name = db.StringProperty()

    app_properties = db.StringListProperty()
    '''
    
    '''

class AApplication():
    '''
    classdocs
    '''

    constants = {'username': 'admin',
                 'password': 'admin'}

    version = '0.1.1'

    data = None

    def __init__(self, name = 'apenAds'):
        '''
        Constructor
        '''

        if self.data is None:
            self.data = OApplication(key_name = 'application', app_name = name)
            self.data.app_version = self.version
            self.data.app_properties = [self.constants.get('username'),
                                        self.constants.get('password')]
        return
        
    def save(self):
        self.data.put()
        
    def load(self):
        key = db.Key.from_path('OApplication', 'application')
        self.data = db.get(key)
        return True
    
    def is_admin(self, username, password):
        if self.data is not None:
            if (self.data.app_properties[0] == username and 
                self.data.app_properties[1] == password):
                return True
            else:
                return False 
        else:
            return False