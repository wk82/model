# -*- coding:utf-8 -*-
'''
Created on 2016-08-08

@author: Administrator
'''


import datetime
import hashlib
import hmac
import requests
import random
import string
import json
from urllib import quote


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def getSignatureKey(key, date_stamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning


def jscdn(url, dir):
    try:

        method = 'POST'

        service = 'cdn'
        region = 'cn-shanghai-1'

        host = 'cdn.api.ksyun.com'
        endpoint = 'http://cdn.api.ksyun.com'

        a = ''.join(random.sample(string.ascii_letters, 5))

        # ak/sk 请从 http://iam.console.ksyun.com/#!/account  获取
        access_key = ""
        secret_key = ""

        content_type = 'application/json'

        data = {"callerReference": 5}
        if url:
            data['files'] = url
        if dir:
            data['dirs'] = dir

        request_parameters = str(json.dumps(data))

        t = datetime.datetime.utcnow()

        amz_date = t.strftime('%Y%m%dT%H%M%SZ')

        date_stamp = t.strftime('%Y%m%d')

        canonical_uri = '/2016-07-11/distribution/invalidation'
        temp_canonical_uri = quote(quote(canonical_uri))

        canonical_querystring = ''

        canonical_headers = 'content-type:' + content_type + '\n' + \
            'host:' + host + '\n' + 'x-amz-date:' + amz_date + '\n'

        signed_headers = 'content-type;host;x-amz-date'

        payload_hash = hashlib.sha256(request_parameters).hexdigest()

        canonical_request = method + '\n' + temp_canonical_uri + '\n' + canonical_querystring + \
            '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = date_stamp + '/' + region + \
            '/' + service + '/' + 'aws4_request'
        string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + \
            '\n' + hashlib.sha256(canonical_request).hexdigest()

        signing_key = getSignatureKey(secret_key, date_stamp, region, service)

        signature = hmac.new(signing_key, (string_to_sign).encode(
            'utf-8'), hashlib.sha256).hexdigest()

        authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + \
            credential_scope + ', ' + 'SignedHeaders=' + \
            signed_headers + ', ' + 'Signature=' + signature

        headers = {'content-type': content_type,
                   'x-amz-date': amz_date,
                   'authorization': authorization_header,
                   'x-action': 'CreateInvalidation',
                   'x-version': '2016-07-11'}

        r = requests.post(endpoint + canonical_uri,
                          data=request_parameters, headers=headers)

        return r.status_code
        # print 'Response code: %d\n' % r.status_code
        # print r.text
    except Exception as e:
        return 'false'

print jscdn(['http://www.duba.com/static/v2/js/bdys.tj.js'], ['http://www.duba.com/static/v2/js/bdys.tj.js'])
