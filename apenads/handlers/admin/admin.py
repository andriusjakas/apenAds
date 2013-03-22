'''
Created on Mar 21, 2013

@author: andrius
'''

def admin_is_logged_in(handler):
    def check(self, *args, **kwargs):
        user = self.session['user']
        if user['valid'] == False:
            self.redirect('/admin')
        else:
            return handler(self, *args, **kwargs)
    return check
