'''
Administrator sites module

@version: 0.1.1
'''
import os
import jinja2

from apenads.objects import AApplication
from apenads.handlers import BaseHandler

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminSiteHandler(BaseHandler):
    
    def get(self):
        self.response.write('list')
        
    def get_new(self):
        self.response.write('new')
        
    def get_edit(self, site_id):
        self.response.write('edit' + site_id)