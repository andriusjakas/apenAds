'''
Admin interface hanlders

@version: 0.1
'''
import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AdminLoginHandler(webapp2.RequestHandler):
    '''
    Admin login page
    '''
    
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())
        return