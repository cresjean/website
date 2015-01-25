import webapp2
from webapp2_extras import routes
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        with open("client/dist/index.html") as html:
            self.response.write(html.read())



application = webapp2.WSGIApplication([
    webapp2.Route('/', MainPage),
    routes.RedirectRoute('/app<:/?>', redirect_to='/app/index.html'),
], debug=True)
