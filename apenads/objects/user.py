'''
User data object and class module

@version: 0.1.1
'''
import random
import string

from google.appengine.ext import db
from apenads.objects.usergroup import OUserGroup
from apenads.objects import AObject

class OUser(db.Model):
    user_id = db.IntegerProperty()
    user_group = db.ReferenceProperty(OUserGroup)
    user_login = db.StringProperty()
    user_password = db.StringProperty()
        
class AUser(AObject):
    
    data = None
    
    def __init__(self, user_id = 0, user_login = 'admin'):
        
        self.data = OUser(key_name = str(user_id))
        self.data.user_id = user_id
        self.data.user_login = user_login
        self.data.user_password = self.gen_password()
        
    def save(self):

        self.data.put()
        
    def gen_password(self, size=12, chars=string.ascii_uppercase + string.digits):
        '''
        Generate random password
        
        @param size: password length (default 12)
        @param chars: list of character used in password
        @return: generated password
        '''
        return ''.join(random.choice(chars) for x in range(size))