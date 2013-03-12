#!/usr/bin/env python
'''
Main bootstrap script
'''
import webapp2

from apenads.handlers import MainHandler
from apenads.handlers.admin import AdminInstallHandler
from apenads.handlers.admin import AdminLoginHandler

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'abb6c50753bf0eb301fa69fc0b13629a',
}

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/admin', AdminLoginHandler),
    ('/install', AdminInstallHandler),
], config=config, debug=True)
