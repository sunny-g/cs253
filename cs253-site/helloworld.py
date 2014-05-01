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
#
'''
HOW WEBAPP2 WORKS

when a request is received to a resource, 
    an instance of RequestHandler is created
    get is called, which makes available info about the request (self.request)
    get() sets properties on self.response, then exits. 

'''
import webapp2

form = '''
    <form method='post' action='/testform'>
        <input name='q'>
        <input type='submit'>
    </form>
'''

# defines a class of type RequestHandler
# this will define the responses to requests for '/'
# get method writes headers and the response to the MainPage response obj
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'     # the default
        self.response.out.write('Hello, Udacity!!!' + '<br>' + form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        ''' for testing:'''
        self.response.headers['Content-Type'] = 'text/plain' 
        self.response.out.write(self.request)
        
        # set q to what was gotten under the name 'q'
        # query = self.request.get('q')
        # self.response.out.write('Your testform input was: ' + query)

app = webapp2.WSGIApplication([ ('/', MainPage), 
                                ('/testform', TestHandler)], 
                                debug=True)
# 
