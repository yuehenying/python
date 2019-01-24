from collections import deque
#把列表当作队列使用，先进先出
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)