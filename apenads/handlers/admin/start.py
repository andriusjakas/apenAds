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
        # main template
        template = jinja_environment.get_template('templates/main.html')
        
        # render
        self.response.write(template.render())
