'''
Created on Mar 21, 2013

@author: andrius
'''

from apenads.handlers import BaseHandler

class AdminBaseHandler(BaseHandler):
    '''
    classdocs
    '''
    
    
    def dispatch(self):
        
        
        
        if self.session.get('user'):
            super(AdminBaseHandler, self).dispatch()
        else:
            self.redirect('/admin')

        