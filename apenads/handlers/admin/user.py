'''
Created on Mar 13, 2013

@author: andrius
'''
import os
import jinja2
from apenads.handlers import BaseHandler
from apenads.objects import AUser

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminUserHandler(BaseHandler):

    def get(self):
        user = AUser()
        # get groups
        template_values = {'data': user.list()}
        
        # load template
        template = jinja_environment.get_template('templates/user.html')
        
        # render
        self.response.write(template.render(template_values))
    
    def post(self):
        pass