#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-19 16:38:47
# @Author  : vision (119018295@qq.com)
# @Link    : http://localhost:5000
# @Version : $Id$

import requests
import json
import datetime
import sys
import httplib
import urllib
import urllib2
import hashlib
import json
import httplib
import urlparse
reload(sys)     #重新载入模块
sys.setdefaultencoding('utf-8') #设置编码


def _verfy_ac(private_key, params):
    items = params.items()
    items.sort()

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)

    params_data = params_data + private_key

    '''use sha1 to encode keys'''
    hash_new = hashlib.sha1()
    hash_new.update(params_data)
    hash_value = hash_new.hexdigest()
    return hash_value


class UConnection(object):
    def __init__(self, base_url):
        self.base_url = base_url
        o = urlparse.urlsplit(base_url)
        if o.scheme == 'https':
            self.conn = httplib.HTTPSConnection(o.netloc)
        else:
            self.conn = httplib.HTTPConnection(o.netloc)

    def __del__(self):
        self.conn.close()

    def get(self, resouse, params):
        resouse += "?" + urllib.urlencode(params)
        print("%s%s" % (self.base_url, resouse))
        self.conn.request("GET", resouse)
        response = json.loads(self.conn.getresponse().read())
        return response


class UcloudApiClient(object):
    # 添加 设置 数据中心和  zone 参数

    def __init__(self, base_url, public_key, private_key, project_id):
        self.g_params = {}
        self.g_params['PublicKey'] = public_key
        self.private_key = private_key
        self.project_id = project_id
        self.conn = UConnection(base_url)

    def get(self, uri, params):
        # print params
        _params = dict(self.g_params, **params)

        if self.project_id:
            _params["ProjectId"] = self.project_id
            print '>>>>>>', _params["ProjectId"]
        _params["Signature"] = _verfy_ac(self.private_key, _params)
        return self.conn.get(uri, _params)

# 实例化 API 句柄


def ucloudreq():
    public_key = "Hx2ovVASgAtKN6i1MkewgTK9zxdlTf4DvjD/Uy/U8mR10hITMa6OYg=="
    private_key = "2670f15db3ee170c7bafdf87ff100d98ef57489b"
    project_id = "org-tz1mz4"  # 项目ID 请在Dashbord 上获取
    base_url = "https://api.ucloud.cn"
    ApiClient = UcloudApiClient(base_url, public_key, private_key, project_id)
    Parameters = {"Action": "RefreshUcdnDomainCache", "DomainId": "ucdn-1mioez", "Type": "file", "UrlList.0": "http://hotnews.duba.com/minisite/1339/"
                  }
    response = ApiClient.get("/", Parameters)
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

with open(r"domain.txt") as f:
    a = {i.split(':')[0]: i.strip().split(':')[1] for i in f}
    if a.get('http://www.duba.com/static/v2/js/bdys.tj.js'):
        print a['http://www.duba.com/static/v2/js/bdys.tj.js']
