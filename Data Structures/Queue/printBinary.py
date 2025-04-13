from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    def front(self):
        i = 0
        while len(self.queue) != 0 and i < 10:
            last = self.queue.pop()
            print(last)
            q.enqueue(last+"0")
            q.enqueue(last+"1")   
            i+=1

    def enqueue(self,item):
        self.queue.appendleft(item)
        

q = Queue()
q.enqueue("1")
q.front()

#FLOW
# append 1
# pop 1 
# append 1+0 =10
# append 1+1 = 11
# pop 10 
# append 10+0 = 100
# append 10+1 = 101
# pop 11