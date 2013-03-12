'''
Created on Mar 12, 2013

@author: andrius
'''

from google.appengine.ext import db

class AUser(db.Model):
    user_id = db.IntegerProperty()
    user_login = db.StringProperty()
    user_password = db.StringProperty()
        