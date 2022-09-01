#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: flask_demo
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-09-01 20:48
'''



from flask import Flask
# from flask_cors import CORS
from flask import request
from flask import jsonify
# import jsonify

app=Flask(__name__)
# CORS(app,supports_credentials=True)


@app.route("http://192.168.174.100/login",methods=["get","post"])
def login():
    username=request.form.get("username")
    pwd=request.form.get("pwd")
    tel=request.form.get("tel")

    data={
        "username":username,
        "pwd":pwd,
        "tel":tel
    }

    return jsonify({"res":1})

if __name__ == '__main__':
    app.run()
