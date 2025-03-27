from collections import deque
import threading
# print(dir(deque))
import time

class Queue:
    
    def __init__(self):
        self.queue = deque()

    def placeOrder(self, orders):
        for order in orders:
            # print("Order is placed",order)
            # print("0.5s delay")
            time.sleep(0.5)
            self.queue.appendleft(order)
        


    def serveOrder(self):
        print("1s delay")
        time.sleep(1)
        while len(self.queue) != 0:
            if len(self.queue) == 0:
                break
            served = self.queue.pop()
            print("Order served",served)
            print(q.queue)
            print("2s delay")
            time.sleep(2)

    
q = Queue()
orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target=q.placeOrder, args=(orders,))
t2 = threading.Thread(target=q.serveOrder)

t1.start()
t2.start()


