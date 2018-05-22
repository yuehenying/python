import requests
import json
import os
import urllib

response = requests.get("http://pvp.qq.com/web201605/js/herolist.json")

hero_json = json.loads(response.text)
hero_num = len(hero_json)

save_dir = 'C:\Users\\asus\Desktop\wangzhe\skins\\'
if not os.path.exists(save_dir):
	os.mkdir(save_dir)

for i in range(hero_num):

	skin_names = hero_json[i]['skin_name'].split('|')

	for cnt in range(len(skin_names)):
		
		save_file_name = save_dir + str(hero_json[i]['ename']) + '-' + hero_json[i]['cname'] + str(cnt+1) + '.jpg';
		skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_json[i]['ename']) + '/' + str(hero_json[i]['ename']) + '-bigskin-' + str(cnt+1) + '.jpg'

		if not os.path.exists(save_file_name):
			urllib.urlretrieve(skin_url,save_file_name)
