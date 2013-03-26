'''
Administrator logout module

@version: 0.1
'''
import os
import jinja2

from apenads.objects import AApplication
from apenads.handlers import BaseHandler

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminLogoutHandler(BaseHandler):
    '''
    Admin login handler class
    '''
    
    def get(self):
        '''
        
        '''
        # check for installed app
        app = AApplication()
        app.data.app_name = self.request.get('app_name')
        
        if not app.data.app_valid:
            self.redirect('/admin')