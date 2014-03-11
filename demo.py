import flask, flask.views
import os
import functools
app = flask.Flask(__name__)
app.secret_key = "bacon"

users = {'jake':'bacon'}
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import os
import re 
import sys
from BeautifulSoup import BeautifulSoup, NavigableString
import httplib2
from multiprocessing import Process
opener = urllib2.build_opener()
from timeout import timeout
urllib2.install_opener(opener)

def getdata(url):
    soup = str((urllib2.urlopen(url).read()))
    xml=re.search('file=(.*?)"', soup).group(1)
    print xml
    mp3 = str((urllib2.urlopen(xml).read()))
    data=str(str(BeautifulSoup(mp3).findAll('location')[0]).split('<![CDATA[')[1]).split(']]')[0]
    infor=str(str(BeautifulSoup(mp3).findAll('info')[0]).split('<![CDATA[')[1]).split(']]')[0]
    print data
    title=str(str(str(BeautifulSoup(mp3).findAll('title')[0]).split('<![CDATA[')[1]).split(']]')[0]).strip()
    return (data,title,infor)
        

    
class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
    def post(self):
  
        username = flask.request.form['username']
        if str(username).strip()=='' or 'http' not in str(username):
            return flask.render_template('index.html')
        else:
            print username
            link=getdata(username)
            #return '{% extends "base.html" %}{% block body %}<a href="'+link[0]+'"> '+link[1]+' </a>{%endblock%}'
            return flask.render_template('index.html',title=link[1],value=str(link[0]).replace('://', '://download.'),
                                         link=link[2])
app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])

app.debug = True
cmd = "kill -9 `fuser -n tcp 15000`"
os.system(cmd)
app.run()
