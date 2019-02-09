# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:41:11 2019

@author: edizh
"""


#from flask import Flask, Response
#import os.path
import importlib.util
importlib.util.spec_from_file_location("module.name", "/path/to/file.py")


app = Flask(__name__)

def get_file(filename):
    try:
        src = os.getcwd() + r"\\" + filename
        return open(src).read()
    except IOError as exc:
        return str(exc)

#Main page
@app.route("/")
def hello():
    return "Hello World!"

#test subpage
@app.route("/test")
def testpage():
    content = get_file("/Frontend/testfile.html")
    return Response(content, mimetype="text/html")


if __name__ == "__main__":
    app.run()

