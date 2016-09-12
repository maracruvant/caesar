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
import webapp2
import cgi
from caesar import encrypt
page_head = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    """

user_input = """
<body>
    <div>
        <form action="/encrypt" method="POST">
            <label for="message">Please type message to encrypt</label>
            <input type="text" name="message"/>
            <br>
            <label for="quantity">Please type rotation amount</label>
            <input type="number" name="quantity"/>
            <button >submit</button>
</body>
"""
class MainHandler(webapp2.RequestHandler):

    def get(self):
        user_input
        self.response.write(page_head + user_input)

class EncryptHandler(webapp2.RequestHandler):
    def post(self):
        text_to_translate = self.request.get("message")
        #default rotation = 13 if no "quantity" is entered or changed
        rot = 13
        #this will be used if  "quantity" != ''
        number_shift = self.request.get("quantity")
        if number_shift == "":
            number_shift = rot
        number_shift = int(number_shift)
        #error message if no text is entered
        error = "<p>You need to write some text!</p>"
        if text_to_translate == "":
            self.response.write(page_head + error + user_input)

        translated_text = encrypt(text_to_translate, number_shift)
        self.response.write(translated_text)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/encrypt', EncryptHandler)
], debug=True)
