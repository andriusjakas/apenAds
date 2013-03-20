'''
Application object module

@version: 0.1.1
'''

import hashlib
import random
import string

from google.appengine.ext import db

APP_PROPERTY_ADMIN_USERNAME = 0
APP_PROPERTY_ADMIN_PASSWORD = 1

class OApplication(db.Model):
    '''
    Application object data
    '''
    
    app_name = db.StringProperty()
    '''
    Appliction name
    '''    
    
    app_key = db.StringProperty()
    '''
    
    '''
    
    app_version = db.StringProperty()
    '''
    Appication version
    '''

    app_valid = db.BooleanProperty()
    '''
    
    '''
    
    app_properties = db.StringListProperty()
    '''
    
    '''

class AApplication():
    '''
    Application object
    '''

    constants = {'username': 'admin',
                 'password': 'admin'}
    '''
    Constants
    '''

    version = '0.1.1'
    '''
    Version
    '''

    data = None
    '''
    
    '''

    def __init__(self, name = 'apenAds'):
        '''
        Constructor
        '''

        # load
        self.load()

        # Instantiate
        if self.data is None:
            self.data = OApplication(key_name = 'application', app_name = name)
            
            # gen app key
            key = hashlib.md5()
            key.update(self.gen_key())
            
            self.data.app_key = key.hexdigest()
            self.data.app_version = self.version
            
            # gen password hash
            key_passwd = hashlib.md5() 
            key_passwd.update(self.constants.get('password'))
            self.data.app_properties = [self.constants.get('username'),
                                        key_passwd.hexdigest()]
        
    def save(self):
        self.data.put()
        
    def load(self):
        key = db.Key.from_path('OApplication', 'application')
        self.data = db.get(key)
    
    def gen_key(self, size=12, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    
    def is_login(self, username, password):
        if self.data is not None:
            key_passwd = hashlib.md5()
            key_passwd.update(password)
            if (self.data.app_properties[0] == username and 
                self.data.app_properties[1] == key_passwd.hexdigest()):
                return True
            else:
                return False 
        else:
            return False