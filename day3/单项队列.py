#单项队列queue
import queue
q = queue.Queue()
q.put('123')
q.put('678')
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())

# 输出结果
# 2
# 123
# 678
