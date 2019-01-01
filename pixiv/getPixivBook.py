import requests
from bs4 import BeautifulSoup
import re

links = []
names = []
page = 1
proxy = '127.0.0.1:25378'   #自己设置代理服务器地址
localPath = r'E:\pictures\P站\\'  #图片保存的路径
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'cookie': '', #自己的cookie，这里我就不放自己的cookie了
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'
}
proxies = {
    'https': proxy
}
def download():
    global page,url
    url = 'https://www.pixiv.net/bookmark.php?rest=show&p='+str(page)
    res = requests.get(url = url,headers = headers,proxies = proxies)
    soup = BeautifulSoup(res.text,'html.parser')
    linkList = soup.select('._layout-thumbnail .ui-scroll-view')
    titleList = soup.select('.image-item .title') 

    for link in linkList:
        link = link['data-src'].replace('c/150x150/','')
        links.append(link)

    for t in titleList:
        t = t['title'].replace('\\','')
        names.append(t)
    
    if page < 6:
        page = page + 1
        download()
    
def savePicture():
    for (pic,name) in zip(links,names):
        res = requests.get(url = pic,headers = headers,proxies = proxies,timeout = 3)
        with open(localPath+name+'.jpg','wb') as f:
            f.write(res.content)
            print(name+'下载完毕')
    
download()
savePicture()
