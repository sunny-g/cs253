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

import webapp2
import routes
from validator import *

signup_form = '''
<div class="signup">
<form method="post">

  <h2>Signup Page (do not use with real passwords!)</h2>
  <label>
    Desired username
    <input type="text" name="username" value="%(username)s">
      <span style="color: red">%(username-error)s</span>
    <br/>
  </label>
  <label>
    Password
    <input type="password" name="password">
    <span style="color: red">%(password-error)s</span>
    <br/>
  </label>
  <label>
    Verify Password
    <input type="password" name="verify">
    <span style="color: red">%(verify-error)s</span>
    <br/>
  </label>
  <label>
    E-mail (optional)
    <input type="text" name="email" value="%(email)s">
    <span style="color: red">%(email-error)s</span>
    <br/>
  </label>

  <input type="submit">

</form>
</div>
'''

welcomePage = '''
<h1>Welcome to the website, %(username)s!</h1>
'''

class User():
    def __init__(self):
        self.username
        self.password
        self.verify
        self.email

class MainPage(webapp2.RequestHandler):
    # since we use regex to process inputs (not iter over chars
    #   in the POST), we need to escape them here instead
    def write_form(self, username="", email="", username_error="", password_error="", verify_error="", email_error=""):
        # we don't include password or verify since we don't want
        #   to return them at all
        self.response.out.write(signup_form % {
            "username-error":   username_error,
            "password-error":   password_error,
            "verify-error":     verify_error,
            "email-error":      email_error,
            "username":         username,
            "email":            email
        })

    def get(self):
        self.write_form()

    def post(self):
        # should you use classes? why?
        #   if you had multiple users and multiple functions
        #       that ran on the same data, it would make sense
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify =   self.request.get('verify')
        user_email  =   self.request.get('email')

        boolUser = valid_username(user_username)
        boolPass = valid_pass(user_password)
        boolVerify = valid_verify(user_password, user_verify)
        boolEmail = valid_email(user_email)

        ## you could create the dict with errors instead of
        #   creating it beforehand with a separate array for
        #   the error's states
        errorDict = {
            "username_error": "That's not a valid username",
            "password_error": "That's not a valid password",
            "verify-error": "Your passwords didn't match",
            "email-error": "That's not a valid email"
        }

        write_errors = ["", "", "", ""]
        if not boolUser:
            write_errors[0] = errorDict["username_error"]
        if not boolPass:
            write_errors[1] = errorDict["password_error"]
        if not boolVerify:
            write_errors[2] = errorDict["verify-error"]
        if not boolEmail and user_email != "":
            write_errors[3] = errorDict["email-error"]

        # if we have no errors, redirect to welcome page
        if write_errors == ["", "", "", ""]:
            self.redirect(routes.welcome + '?username=' + user_username)
        else:
            self.write_form(user_username, user_email, *write_errors)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        # when the user gets redirected, they GET a page for a
        # particular username using the username="" URL query
        # this is what we GET here and validate
        user_username = self.request.get('username')
        if valid_username(user_username):
            self.response.out.write(welcomePage % {'username': user_username})
        else:
            self.redirect(routes.signup)

# the application
app = webapp2.WSGIApplication([
    (routes.signup,         MainPage),
    (routes.welcome,        WelcomeHandler)],
    debug=True)
