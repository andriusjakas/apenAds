'''
Administrator login module

@version: 0.1
'''
import os
import jinja2

from apenads.handlers import BaseHandler

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminLoginHandler(BaseHandler):
    '''
    Admin login handler class
    '''
    
    def get(self):
        '''
        
        '''
        
        # load template
        template = jinja_environment.get_template('templates/index.html')
        
        # render
        self.response.write(template.render())
    
    def post(self):
        '''
        
        '''
        
        
        self.response.write(self.request.get('username'))
        return

