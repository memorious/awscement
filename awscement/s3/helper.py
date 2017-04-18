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
__module_name__ = "cement.s3.helper"

#let's load up boto3
import boto3
import os

#let's import main helper
from awscement.helper import *

def s3Connect(self):
    if self.app.pargs.key_id is None:
        print(toLine('Enter AWS Access Key ID'))
        return None
    if self.app.pargs.access_key is None:
        print(toLine('Enter AWS Secret Access Key'))
        return

    #let's start a connection
    s3 = boto3.resource(
        's3',
        aws_access_key_id = self.app.pargs.key_id,
        aws_secret_access_key = self.app.pargs.access_key)   #lets connect using credentials and region stored in ~/.aws/credentials and ~/.aws/config

    return s3

def s3Count(self, s3):
    fileList = s3List(self, s3)
    if(fileList):
        return str(len(fileList))
    else:
        return "0"

def s3List(self, s3):
    if self.app.pargs.bucket is None:
        print(toLine('Enter target Bucket'))
        return None
    if self.app.pargs.dir is None:
        print(toLine('No target directory entered'))
        self.app.pargs.dir = ''
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

def s3Upload(self, s3):
    if self.app.pargs.filename is None:
        print(toLine('Enter a file to upload to bucket'))
        return None
    if self.app.pargs.bucket is None:
        print(toLine('Enter target Bucket'))
        return None
    if self.app.pargs.dir is None:
        print(toLine('No target directory entered'))
        self.app.pargs.dir = ''
    else:
        self.app.pargs.dir = self.app.pargs.dir + "/"
    #let's find our bucket
    if s3.Bucket(self.app.pargs.bucket) in s3.buckets.all():
        bucket = s3.Bucket(self.app.pargs.bucket)
    else:
        print(toLine('Target Bucket Not Found'))
        return None

    # s3.meta.client.upload_file(self.app.pargs.filename, self.app.pargs.bucket, self.app.pargs.filename)
    full_file_path = self.app.pargs.filename.split('/')
    filename = self.app.pargs.dir + full_file_path[-1]
    print(self.app.pargs.filename);
    with open(self.app.pargs.filename, 'rb') as data:
        bucket.upload_fileobj(data, filename)

def s3Download(self, s3):
    if self.app.pargs.filename is None:
        print(toLine('Enter a file to download from bucket'))
        return None
    if self.app.pargs.bucket is None:
        print(toLine('Enter target Bucket'))
        return None
    if self.app.pargs.dir is None:
        print(toLine('No target directory entered'))
        self.app.pargs.dir = ''
    else:
        self.app.pargs.dir = self.app.pargs.dir + "/"

    file_path = self.app.pargs.dir

    if s3.Bucket(self.app.pargs.bucket) in s3.buckets.all():
        bucket = s3.Bucket(self.app.pargs.bucket)
    else:
        print(toLine('Target Bucket Not Found'))
        return None

    for obj in bucket.objects.all():
        if file_path in obj.key:
            #let's create our local folder(s) if they don't exist
            if not os.path.exists("media/" + file_path):
                os.makedirs("media/" + file_path)

            full_file_path = "media/" + file_path + self.app.pargs.filename
            with open(full_file_path, 'wb') as data:
                bucket.download_fileobj(obj.key, data)
