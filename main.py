
from google.appengine.ext import webapp  
from google.appengine.ext.webapp import util
import cgi  
import datetime

class MainHandler(webapp.RequestHandler):
    def get(self):
        birthdate_str = self.request.get('birthdate')
        age_result = ''
        if birthdate_str:
            try:
                birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')
                today = datetime.datetime.today()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                age_result = "{} years".format(age)
            except ValueError:
                age_result = 'Invalid date format. Use YYYY-MM-DD.'

        html_content = """
            <html>
              <head>
              <meta content='50;url=http://agecalculator.blogspot.com/' http-equiv='refresh'/>
              <title>Age Calculator</title></head>
              <body>
                <h2>Simple Age Calculator</h2>
                <form method="get">
                  <label for="birthdate">Enter your birthdate (YYYY-MM-DD):</label><br/>
                  <input type="text" name="birthdate" value="%s" size="30"/>
                  <input type="submit" value="Calculate Age"/>
                </form>
                <p><strong>Age:</strong> %s</p>
              </body>
            </html>
        """ % (cgi.escape(birthdate_str), cgi.escape(age_result))

        self.response.out.write(html_content)

def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
