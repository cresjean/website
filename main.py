import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        with open("client/dist/index.html") as html:
            self.response.write(html.read())



application = webapp2.WSGIApplication([
    webapp2.Route('/', MainPage),
], debug=True)
