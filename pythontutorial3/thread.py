import threading

def shadow(num):
    print('{}产生了第{}个分身'.format(threading.currentThread().getName(),num))

for i in range(1,6):
    t = threading.Thread(target=shadow,args=(i,),name='第{}个鸣人'.format(i))
    t.start()
    t.join()

print(threading.currentThread().getName())