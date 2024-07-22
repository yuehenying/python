import json

fr=open("csv_to_json\data.csv","r",encoding='gbk')
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(","))
fr.close()
fw=open("csv_to_json\data.json","w",encoding='gbk')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
b = json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
print(b)
fw.write(b)
fw.close()
