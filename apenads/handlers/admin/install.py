'''
Admin install handler module

@version: 0.1.1
'''
import os
import jinja2

from apenads.handlers import BaseHandler
from apenads.objects import AApplication
from apenads.objects import AUserGroup
from apenads.objects import AUser

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
        
        # create app
        app = AApplication()
        
        # set values
        template_values = {'app_name': app.data.app_name,
                           'app_key': app.data.app_key,
                           'app_version': app.data.app_version,
                           }        
        
        if app.data.app_valid:
            template = jinja_environment.get_template('templates/installed.html')
            
        else:
            template = jinja_environment.get_template('templates/install.html')
        
        # render
        self.response.write(template.render(template_values))            
        
    def post(self):
        
        app = AApplication()
        app.data.app_name = self.request.get('app_name')
        app.data.app_valid = True
        app.save()
        
        grp = AUserGroup()
        grp.save()
        
        usr = AUser()
        usr.save()
        
        template_values = {'app_name': app.data.app_name,
                           'app_key': app.data.app_key,
                           'app_version': app.data.app_version,
                           }         
        
        template = jinja_environment.get_template('templates/installed.html')
        
        # render
        self.response.write(template.render(template_values))
