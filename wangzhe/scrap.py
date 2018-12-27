import requests
import json
import os

response = requests.get("http://pvp.qq.com/web201605/js/herolist.json")

hero_json = json.loads(response.text)
hero_num = len(hero_json)

# save_dir的路径请自己定义，这里末尾必须得多加个\因为不允许末尾只有\
save_dir = r'E:\pictures\wangzhe\\'
if not os.path.exists(save_dir):
	os.mkdir(save_dir)

for i in range(hero_num):

	skin_names = hero_json[i]['skin_name'].split('|')

	for cnt in range(len(skin_names)):
		
		save_file_name = save_dir + str(hero_json[i]['ename']) + '-' + hero_json[i]['cname'] + str(cnt+1) + '.jpg'
		skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_json[i]['ename']) + '/' + str(hero_json[i]['ename']) + '-bigskin-' + str(cnt+1) + '.jpg'
		img = requests.get(skin_url)
		#默认为r可省略表示只读，因为要写入所以open第二个参数得为wb
		with open(save_file_name,'wb') as f:
			f.write(img.content)
			print(save_file_name+'下载完成')