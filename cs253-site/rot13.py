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

rot13_form = '''
    <form method="post">
        <label>
            <h2>Enter some text that you want ROT13-ed:</h2>
            <textarea name="text" rows="6" cols="50">%(textbox)s</textarea>
            <br/>
            <input type="submit">
        </label>
    </form>
'''

def rot13(input_string):
    new_str = ""
    upperAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in input_string:
        case = char.isupper()
        char = char.upper()
        if char not in upperAlpha:
            new_str += cgi_escape_html(char)
        else:
            i = (upperAlpha.find(char) + 13) % 26
            if case:
                new_str += upperAlpha[i]
            else:
                new_str += upperAlpha[i].lower()
    return new_str

class MainPage(webapp2.RequestHandler):
    # we don't escape here b/c it will only output ciphertext as
    #   "" or what it gets from a POST request, which is escaped
    def write_form(self, ciphertext=""):
        self.response.out.write(rot13_form % { "textbox": ciphertext})

    def get(self):
        self.write_form()

    def post(self):
        plaintext = self.request.get('text')
        ciphertext = rot13(plaintext)
        self.write_form(ciphertext)


# the application
app = webapp2.WSGIApplication([
    (routes.rot13,               MainPage)],
    debug=True)
