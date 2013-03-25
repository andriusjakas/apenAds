'''
Administrator start page module

'''
import os
import jinja2

from apenads.handlers import BaseHandler
from apenads.handlers.admin.admin import admin_is_logged_in

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminStartHandler(BaseHandler):
    '''
    Admin interface start page
    
    @version: 0.1.1
    '''
    
    @admin_is_logged_in
    def get(self, **kwargs):
        '''
        Process GET
        '''
        # session
        user = self.session['user']
      
        # main template
        template_values = {'user': {'name': user['username']},
                           }
        template = jinja_environment.get_template('templates/start.html')
        
        # render
        self.response.write(template.render(template_values))
