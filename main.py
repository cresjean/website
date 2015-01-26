import webapp2
from google.appengine.api import mail, taskqueue
from random import randrange
from ds import Code
import logging
import json
from webapp2_extras import routes

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        with open("client/dist/index.html") as html:
            self.response.write(html.read())


class API(webapp2.RequestHandler):
    def get_code_stats(self):

        code_stat = Code.get_one()
        if code_stat is None:
            logging.info("Code stat is none")
            code_stat = Code(lines=randrange(8000, 9000), commits=randrange(100, 200), pr=randrange(30, 90))
            code_stat.put()
        else:
            logging.info("Code stat exist")
            code_stat.lines = code_stat.lines + randrange(50)
            code_stat.commits = code_stat.commits + randrange(10)
            code_stat.pr = code_stat.pr + randrange(2)
            code_stat.put()

        self.response.headers.add("Content-Type", "application/json")

        self.response.write(json.dumps({"stat_lines": code_stat.lines,
                                        "stat_commits": code_stat.commits,
                                        "stat_pulls": code_stat.pr}))


    def contact_me(self):
        logging.debug(self.request.body)
        msg = json.loads(self.request.body)
        if msg.get('c_email') and msg.get('c_name') and msg.get('c_message') and mail.is_email_valid(msg.get('c_email')):

            mail.send_mail("crespo@crespowang.com", "hotpuma@gmail.com", "Message from {}".format(msg.get('c_email')), msg.get('c_message'), bcc="crespo@crespowang.com")

        self.response.write(json.dumps({"sendstatus": 1, "message": "Thanks! I will be in touch with you in the next 24 hours"}))

    def just_ok(self, junk):
        self.response.write("OK")



application = webapp2.WSGIApplication([
    webapp2.Route('/', MainPage),
    webapp2.Route('/plugins/<:.*>', API, handler_method='just_ok', methods=['GET']),
    routes.RedirectRoute('/app<:/?>', redirect_to='/app/index.html'),
    routes.PathPrefixRoute('/api', [
        webapp2.Route('/code', API, handler_method='get_code_stats', methods=['GET']),
        webapp2.Route('/contact-me', API, handler_method='contact_me', methods=['POST']),
    ])

], debug=True)
