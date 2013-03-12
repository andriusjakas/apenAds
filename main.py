#!/usr/bin/env python
import webapp2

from apenads.admin.handlers import AdminLoginHandler

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('apenAds')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/admin', AdminLoginHandler),
], debug=True)
