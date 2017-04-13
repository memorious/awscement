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

import time

timeval = time.strftime("%c")

def toLine(valueToPrint):
    return(timeval + " : " + valueToPrint)

def s3Connect(self):
    if self.app.pargs.key_id is None:
        print(toLine('Enter AWS Access Key ID'))
        return None
    if self.app.pargs.access_key is None:
        print(toLine('Enter AWS Secret Access Key'))
        return
    #let's load up boto3
    import boto3
    #let's start a connection
    s3 = boto3.resource(
        's3',
        aws_access_key_id = self.app.pargs.key_id,
        aws_secret_access_key = self.app.pargs.access_key)   #lets connect using credentials and region stored in ~/.aws/credentials and ~/.aws/config

    return s3

def s3List(self, s3):
    if self.app.pargs.bucket is None:
        print(toLine('Enter target Bucket'))
        return None
    if self.app.pargs.dir is None:
        print(toLine('No target directory entered'))

    #let's find our bucket
    if s3.Bucket(self.app.pargs.bucket) in s3.buckets.all():
        bucket = s3.Bucket(self.app.pargs.bucket)
    else:
        print(toLine('Target Bucket Not Found'))
        return None

    fileList = []
    if self.app.pargs.dir is None:
        for obj in bucket.objects.all():
            filepath = obj.key.split('/')
            filename = filepath[-1]
            fileList.append(filename)
    else:
        for obj in bucket.objects.all():
            if self.app.pargs.dir in obj.key in obj.key:
                filepath = obj.key.split('/')
                filename = filepath[-1]
                fileList.append(filename)

    return fileList
