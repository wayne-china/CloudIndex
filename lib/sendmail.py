#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import smtplib
import sys
import email
from email.mime.text import MIMEText
import requests

charset = 'utf-8'

url="http://sendcloud.sohu.com/webapi/mail.send.json"

def send(reciver ):
    params = {"api_user": "", \
       "api_key" : "",\
       "to" : reciver, \
       "from" : "",
       "subject" : "CloudIndex注册通知", \
       "html": "您好：<br>"
               "&nbsp &nbsp 欢迎您注册 CloudIndex ，这是一封由系统自动发出的邮件。如果您没有注册CloudIndex，请忽视本邮件。<br>" \
               "<center><a href='cloudindex.club'>CloudIndex.club</a></center>" \
    }    
    try:
        r = requests.post(url, files={}, data=params)
        print r.text   
    except Exception,e:
        print(e)
        return False


def forget(mail_content,reciver):
    params = {"api_user": "", \
       "api_key" : "",\
       "to" : reciver, \
       "from" : "",
       "subject" : "重置密码通知", \
       "html": mail_content, 
    }    
    try:
        r = requests.post(url, files={}, data=params)
        print r.text   
    except Exception,e:
        print(e)
        return False

def notice(mail_content,reciver):
    params = {"api_user": "", \
       "api_key" : "",\
       "to" : reciver, \
       "from" : "",
       "subject" : "有人在CloudIndex提到了您", \
       "html": mail_content, 
    }    
    try:
        r = requests.post(url, files={}, data=params)
        print r.text   
    except Exception,e:
        print(e)
        return False

def reply(mail_content,reciver):
    params = {"api_user": "", \
       "api_key" : "",\
       "to" : reciver, \
       "from" : "",
       "subject" : "有人在CloudIndex上回复了您的话题", \
       "html": mail_content, 
    }    
    try:
        r = requests.post(url, files={}, data=params)
        print r.text   
    except Exception,e:
        print(e)
        return False

