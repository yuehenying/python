#coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()   #未爬取的url列表
        self.old_urls = set()   #已爬取的url列表

    def has_new_url(self):
        return self.new_url_size() != 0
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    def add_new_url(self, url):

        if url is None:
            return None
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    def new_url_size(self):
        return len(self.new_urls)
    
    def old_url_size(self):
        return len(self.old_urls)