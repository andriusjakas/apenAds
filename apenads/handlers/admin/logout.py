'''
Administrator logout module

@version: 0.1
'''
from apenads.handlers import BaseHandler

class AdminLogoutHandler(BaseHandler):
    '''
    Admin logout handler class
    '''
    
    def get(self):
        '''
        
        '''
        # remove session
        self.session['user'] = None
        
        self.redirect('/admin')