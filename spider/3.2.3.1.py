# coding:utf-8
'''
# 简单的get请求
import requests
r = requests.get('http://www.baidu.com')
print r.content
'''

'''
# post请求
import requests
postdata = {'username': 'admin', 'password': 'admin'}
r = requests.post('http://localhost/login.php', data = postdata)
print r.content
'''

# 带参数的get请求
import requests
payload = {'keywords': 'blog:qiyeboy', 'pageindex': 1}
r = requests.get('https://zzk.cnblogs.com/s/blogpost', params = payload)
print r.url


