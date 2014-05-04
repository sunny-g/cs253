#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
HOW WEBAPP2 WORKS

when a request is received to a resource, 
    an instance of RequestHandler is created
    get is called, which makes available info about the request (self.request)
    get() sets properties on self.response, then exits. 

'''
import webapp2
import routes
from validator import *

bday_form = '''
    <form method='post'>
        What is your Date of Birth (DoB)?
        <br>

        <label>
            Month
            <input type='text' name='month' value="%(month)s">
            <br>
        </label>
        <label>
            Day
            <input type='text' name='day' value="%(day)s">
            <br>
        </label>
        <label>
            Year
            <input type='text' name='year' value="%(year)s">
            <br>
        </label>

        <!-- this creates a new line (technically a block element) for our error message which will appear red-->

        <div style="color: red">%(error-div)s</div>

        <br>
        <input type='submit'>
    </form>
'''

# defines a class of type RequestHandler
# this will define the responses to requests for '/'
# get method writes headers and the response to the MainPage response obj
class MainPage(webapp2.RequestHandler):
    # since we use self.reponse.out.write(bday_form) multiple times,
    # lets write a func to do that
    def write_form(self, error="", month="", day="", year=""):
        # by default, all values are is empty
        # so on first page load, this will return "" for all values
        self.response.out.write(bday_form % {
            "error-div": error,
            "month": cgi_escape_html(month),
            "day": cgi_escape_html(day),
            "year": cgi_escape_html(year)
        })

    def get(self):
        # self.response.headers['Content-Type'] = 'text/html'     # text/html is the default
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month_abbr(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        # if any validation fails, return the same form page
        if not (month and day and year):
            self.write_form("That doesn't look like a valid date, please try again", user_month, user_day, user_year)
        else:
            # instead of printing thanks, redirect to /thanks
            self.redirect(routes.bday + "/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Thanks for your valid response!')

# unused, only here to learn from
class TestHandler(webapp2.RequestHandler):
    '''when someone submits input on the form on the main page, this
     RequestHandler is called, which writes out some text including your
     query'''
    def post(self):
        form_query = self.request.get('q')
        self.response.out.write('Your input was: ' + form_query)


# the application
app = webapp2.WSGIApplication([
    (routes.bday,               MainPage),
    (routes.bday + '/thanks',      ThanksHandler)],
    debug=True)

