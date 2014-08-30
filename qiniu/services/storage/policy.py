# -*- coding: utf-8 -*-
import json
import time
import urllib


class PutPolicy(object):
    scope = None
    expires = None
    callbackUrl = None
    callbackBody = None
    returnUrl = None
    returnBody = None
    endUser = None
    asyncOps = None

    saveKey = None
    insertOnly = None
    detectMime = None
    mimeLimit = None
    fsizeLimit = None
    persistentNotifyUrl = None
    persistentOps = None

    def __init__(self, scope, expires=None):

        self.scope = scope
        if expires is None:
            self.expires = 3600
            pass

    def token(self, auth=None):
        if auth is None:
            auth = digest.Mac()

        token = dict(
            scope=self.scope,
            deadline=int(time.time()) + self.expires,
        )

        if self.callbackUrl is not None:
            token["callbackUrl"] = self.callbackUrl

        if self.callbackBody is not None:
            token["callbackBody"] = self.callbackBody

        if self.returnUrl is not None:
            token["returnUrl"] = self.returnUrl

        if self.returnBody is not None:
            token["returnBody"] = self.returnBody

        if self.endUser is not None:
            token["endUser"] = self.endUser

        if self.asyncOps is not None:
            token["asyncOps"] = self.asyncOps

        if self.saveKey is not None:
            token["saveKey"] = self.saveKey

        if self.insertOnly is not None:
            token["exclusive"] = self.insertOnly

        if self.detectMime is not None:
            token["detectMime"] = self.detectMime

        if self.mimeLimit is not None:
            token["mimeLimit"] = self.mimeLimit

        if self.fsizeLimit is not None:
            token["fsizeLimit"] = self.fsizeLimit

        if self.persistentOps is not None:
            token["persistentOps"] = self.persistentOps

        if self.persistentNotifyUrl is not None:
            token["persistentNotifyUrl"] = self.persistentNotifyUrl

        b = json.dumps(token, separators=(',', ':'))
        return mac.sign_with_data(b)


class GetPolicy(object):
    expires = 3600

    def __init__(self, expires=3600):
        self.expires = expires

    def make_request(self, base_url, mac=None):
        '''
         *  return private_url
        '''
        if mac is None:
            mac = digest.Mac()

        deadline = int(time.time()) + self.expires
        if '?' in base_url:
            base_url += '&'
        else:
            base_url += '?'
        base_url = '%se=%s' % (base_url, str(deadline))

        token = mac.sign(base_url)
        return '%s&token=%s' % (base_url, token)


def make_base_url(domain, key):
    '''
     * domain => str
     * key => str
     * return base_url
    '''
    key = rpc.encode_unicode(key)
    return 'http://%s/%s' % (domain, urllib.quote(key))