'''
Admin install handler module
'''
import os
import jinja2

from apenads.handlers import BaseHandler
from apenads.objects import AApplication

# template environment
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminInstallHandler(BaseHandler):
    '''
    
    '''
    
    def get(self):
        '''
        Process GET request
        '''
        
        # check for app data
        app = AApplication()
        app.save()
        
        template = jinja_environment.get_template('templates/install.html')
        self.response.write(template.render())