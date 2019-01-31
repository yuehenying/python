import requests

class DataOutput(object):

    def __init__(self):
        self.filepath = r'E:\pictures\B站' #图片保存的路径
        self.urls = set()

    def store_url(self, url):
        self.urls.add(url)
        if len(self.urls) >= 10 :
            self.store_image(self.filepath)
    
    def store_image(self, path):
        for url in self.urls:   
            res = requests.get(url)
            name = path + '\\' + url[-15:]
            with open(name, 'wb') as f:
                f.write(res.content)
                print(name + '下载完成')
        self.urls = set()