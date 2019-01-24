# coding:utf-8
'''
# 使用fork模块创建多进程
import os
if __name__ == '__main__':
    print 'Current Process (%s) start ...' % (os.getpid())
    pid = os.fork()
    if pid < 0:
        print 'error in fork'
    elif pid == 0:
        print 'I am child process(%s) and my parent process is (%s)',(os.getpid(),os.getppid())
    else:
        print 'I(%s) created a child process(%s).',(os.getpid(),pid)
'''
'''
# 使用multiprocessing模块创建多进程
import os
from multiprocessing import Process 

def run_proc(name):
    print 'Child process %s (%s) Running...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p_list = []
    for i in range(5):
        p = Process(target = run_proc, args = (str(i),))
        p_list.append(p)
        print 'Process will start.' 
        p_list[i].start()
    for p in p_list:   
        p.join()
    print ' Process end.'
'''

'''
# 使用Pool类来代表进程池对象
from multiprocessing import Pool
import os,time,random

def run_task(name):
    print 'Task %s (pid=%s) is running...' % (name,os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' % name

if __name__ == '__main__':
    print 'Current process %s.' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print 'Waiting for all subprocess one...'
    p.close()
    p.join()    #等待所有子进程执行结束
    print 'All subprocess done.'
'''

'''
# 使用Queue实现进程间通信
from multiprocessing import Process,Queue
import os,time,random

def proc_write(q,urls):
    print('Process(%s)is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())

def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue...' % url)

if __name__ == '__main__':
    q = Queue()
    proc_writer1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
    proc_writer2 = Process(target=proc_write,args=(q,['url_4','url_5','url_6']))
    proc_reader = Process(target=proc_read,args=(q,))
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()
    proc_writer1.join()
    proc_writer2.join()
    proc_reader.terminate()
'''
# pipe进程间通信
import multiprocessing
import random
import time,os

def proc_send(pipe,urls):
    for url in urls:
        print 'Process(%s) send: %s' % (os.getpid(),url)
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print 'Process(%s) rev:%s' % (os.getpid(),pipe.recv())
        time.sleep(random.random())

if __name__ == '__main__':
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target = proc_send, args = (pipe[0], ['url_'+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target = proc_recv, args = (pipe[1], ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
