# MIT License
#
# Copyright (c) 2017 memorious
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = "memorious"
__module_name__ = "cement.s3.controller"

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from helper import *

#Let's create our base controller
class s3Controller(CementBaseController):
    class Meta:
        label = 'base'
        description = "s3 controller!"
        arguments = [
            (['--key_id'],
             dict(action='store', help='AWS Access Key ID')),
            (['--access_key'],
             dict(action='store', help='AWS Secret Access Key')),
            (['--filename'],
             dict(action='store', help='Filename To Upload')),
            (['--bucket'],
             dict(action='store', help='Target S3 Bucket')),
            (['--dir'],
             dict(action='store', help='Target S3 Directory')),
            ]

    #default action (nothing really happens here)
    @expose(hide=True)
    def default(self):
        self.app.log.debug('Inside cement.s3.controller.default()')

    #list action (lists files in a bucket('s directory)
    @expose(help="This Command Lists All Files In A Bucket('s directory)")
    def list(self):
        self.app.log.debug("Inside cement.s3.controller.list()")
        #let's make sure we have our credentials and targets
        s3 = s3Connect(self)
        if s3:
            fileList = s3List(self, s3)
            if(fileList):
                for obj in fileList:
                    print(toLine(obj))

    #count action (count files in a bucket('s directory)
    @expose(help="This Command Counts All Files In A Bucket('s directory)")
    def count(self):
        self.app.log.debug("cement.s3.controller.count()")
        s3 = s3Connect(self)
        if s3:
            print(toLine(s3Count(self, s3) + " Object(s) Found"))

    #count action (count files in a bucket('s directory)
    @expose(help="This Command Uploads A File To A Bucket('s directory)")
    def upload(self):
        self.app.log.debug("cement.s3.controller.upload()")
        s3 = s3Connect(self)
        if s3:
            s3Upload(self, s3)

    #count action (count files in a bucket('s directory)
    @expose(help="This Command Downloads A File To A Bucket('s directory)")
    def download(self):
        self.app.log.debug("cement.s3.controller.upload()")
        s3 = s3Connect(self)
        if s3:
            s3Download(self, s3)

class S3Interface(CementApp):
    class Meta:
        label = 's3interface'
        base_controller = 'base'
        handlers = [s3Controller]

with S3Interface() as app:
    app.run()
