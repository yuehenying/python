# coding:utf-8
import urllib2

request = urllib2.Request('https://www.zhihu.com/')
response = urllib2.urlopen(request, timeout = 2)
html = response.read()
print html
