# coding:utf-8
'''
import urllib2
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener([proxy,])
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.zhihu.cn')
print response.read()
'''

import urllib2
proxy = urllib2.ProxyHandler({'http': '119.101.113.172:9999'})
opener = urllib2.build_opener(proxy,)
response = opener.open('http://www.zhihu.com/')
print response.read()