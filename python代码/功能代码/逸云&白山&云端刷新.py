#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-19 16:58:20
# @Author  : vision (119018295@qq.com)
# @Link    : http://localhost:5000
# @Version : $Id$


import requests
import datetime
import sys
import httplib
import urllib
import urllib2
import hashlib
import json

reload(sys)
sys.setdefaultencoding('utf-8')


def exclouds(url, dir):
    '''逸云cdn'''
    try:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        uu = "http://openapi.exclouds.com/contentService/AddRefresh"
        url = ';'.join(url)
        dir = ';'.join(dir)
        if url:
            post_data = {"url": url, "type": 1}
        if dir:
            post_data = {"url": dir, "type": 0}
        data = urllib.urlencode(post_data)
        req = urllib2.Request(uu, data)
        req.add_header("Authorization", "21AC05E22B37C20A0AB3484A942B1021")
        req.add_header("Date", date)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return eval(the_page)['code']
    except Exception as e:
        return 'false'


def isurecloud(url, dir):
    '''云端智度cdn'''
    try:
        token_data = {'grant_type': 'client_credentials',
                      'appid': 'e7e93f814eb03f2fa4f1c2dc060008', 'appsecret': '9434ccefc4'}
        res = requests.post(
            'https://webapi.isurecloud.com/oauth/access_token', data=json.dumps(token_data))
        data = json.loads(res.text)
        token = data.get('result')['access_token']
        refresh_data = {"access_token": token}
        if url:
            refresh_data['files'] = url
        if dir:
            refresh_data['dirs'] = dir
        refresh_url = requests.post(
            'https://webapi.isurecloud.com/content/add_purge', data=json.dumps(refresh_data))
        a = json.loads(refresh_url.text)
        return a.get('status')

    except Exception as e:
        return 'false'


def qingcdn(url):
    '''白山'''
    try:
        payload = {'token': '77992911525d19001c4af62737157b3f', 'method': 'purge.add',
                   'params': {'urls': url}}
        print payload
        res = requests.post('http://api.qingcdn.com/apix',
                            data=json.dumps(payload))

        a = json.loads(res.text)
        if a['errno'] == 0:
            print 'ok'
    except Exception, e:
        print 'timeout'
