import socket
import threading
import time

def dealClient(sock, addr):
    # 4.接收传来的数据，并发送给对方
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Hello,I am server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('--->>%s!' % data.decode('utf-8'))
        sock.send(('Loop_Msg: %s!' % data.decode('utf-8')).encode('utf-8'))

    # 5.关闭套接字
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    # 1.创建基于IPV4和TCP协议的socket套接字绑定IP和端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # 2.监听
    s.listen(5)
    print('Waiting for connetction...')
    while True:
        # 3.接受一个新的连接
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target = dealClient, args = (sock, addr))
        t.start()


