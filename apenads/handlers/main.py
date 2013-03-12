'''
Created on Mar 12, 2013

@author: andrius
'''
from apenads.handlers import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.response.write('')
