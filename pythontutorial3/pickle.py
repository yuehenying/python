try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(url='index.html',title='首页',content='首页')
# dumps将数据序列化
# print(pickle.dumps(d))

# dump可直接将数据序列化后存入文件
f = open(r'1.txt','wb')
pickle.dump(d,f)
f.close()

f = open(r'1.txt','rb')
# 打开文件之后读取里面的信息，再用loads方法反序列化对象
# s = f.read()
# d = pickle.loads(s)
d = pickle.load(f)
print(d)
f.close()