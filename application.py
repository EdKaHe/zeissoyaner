# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:41:11 2019

@author: edizh
"""


from flask import Flask

app = Flask.main(__name__)

@app.route("/")
def hello():
    return "Hello World!"