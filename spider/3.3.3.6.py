# coding:utf-8
import requests
r = requests.get('http://www.github.com')
print r.url
print r.status_code
print r.history