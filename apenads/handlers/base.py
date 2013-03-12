'''
Base handler class
'''
import webapp2

from webapp2_extras import sessions

from apenads.objects import AApplication

class BaseHandler(webapp2.RequestHandler):
    '''
    Base handler class
    
    Base handler class (to be subclassed) with session support
    '''
    
    def dispatch(self):
        '''
        Dispatch request after session save
        '''
        
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
    
    def application(self):
        app = AApplication()
        app.load()
        return app
