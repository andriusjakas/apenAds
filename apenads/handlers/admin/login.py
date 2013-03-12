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
        Authenticate
        '''
        
        if self.application().is_admin(self.request.get('username'), self.request.get('password')):
            self.session['user'] = {'username': self.request.get('username')}
            template = jinja_environment.get_template('templates/main.html')
        else:
            template = jinja_environment.get_template('templates/index.html')
        
        # render
        self.response.write(template.render())
