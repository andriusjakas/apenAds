#!/usr/bin/env python
'''
Main bootstrap script
'''
import webapp2
from webapp2_extras import routes

from apenads.handlers import MainHandler
from apenads.handlers.admin import AdminInstallHandler
from apenads.handlers.admin import AdminLoginHandler
from apenads.handlers.admin import AdminLogoutHandler
from apenads.handlers.admin import AdminStartHandler
from apenads.handlers.admin import AdminUserHandler
from apenads.handlers.admin import AdminSiteHandler

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'abb6c50753bf0eb301fa69fc0b13629a',
}

app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=MainHandler),
    webapp2.Route('/admin', handler=AdminLoginHandler),
    webapp2.Route('/admin/logout', handler=AdminLogoutHandler),
    webapp2.Route('/admin/start', handler=AdminStartHandler),
    webapp2.Route('/admin/site', handler=AdminSiteHandler, name='list', handler_method='get', methods=['GET']),
    webapp2.Route('/admin/site/new', handler=AdminSiteHandler, name='new', handler_method='get_new', methods=['GET']),
    webapp2.Route('/admin/site/<site_id:\d+>', handler=AdminSiteHandler, name='edit', handler_method='get_edit', methods=['GET']),
    webapp2.Route('/admin/user', handler=AdminUserHandler),
    webapp2.Route('/install', handler=AdminInstallHandler),
], config=config, debug=True)
