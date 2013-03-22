'''
Created on Mar 21, 2013

@author: andrius
'''
import webapp2
from apenads.handlers import BaseHandler

def admin_is_logged_in(handler):
    def check(self, *args, **kwargs):
        user = self.session['user']
        webapp2.logging.info(user['valid'])
        if user['valid'] == False:
            self.redirect('/admin')
        else:
            return handler(self, *args, **kwargs)
    return check

class AdminBaseHandler(BaseHandler):
    '''
    classdocs
    '''
    
    
    def dispatch(self):
        
        
        
        if self.session.get('user'):
            super(self.__class__.__name__, self).dispatch()
        else:
            self.redirect('/admin')

        