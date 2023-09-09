class MyCircularQueue(object):

    def __init__(self, k):
        self.data = [0]*k
        self.n = k
        self.front,self.rear = -1,-1
        

    def enQueue(self, value):
        # 1.) CQ is full when rear is one behind the front
        if self.isFull():
            return False
        # 2.) if front is -1 then list is initially empty make it 0
        if self.front ==-1:
            self.front = 0
        # 3.) Move the rear Pointer so as to store the new Value
        self.rear = (self.rear+1)%self.n
        self.data[self.rear] = value
        return True
        

    def deQueue(self):
        # 1.) CQ if empty can't dequeue
        if self.isEmpty():
            return False
        # 2.) store the res to return if needed
        res = self.data[self.front]
        # 3.) If only one node present, make front & rear as -1
        if self.front == self.rear:
            self.front = self.rear =-1
        # 2.) Move the front Pointer
        else:
            self.front = (self.front+1)%self.n
        return True




    def Front(self): # T(n): O(1)
        return -1 if self.isEmpty() else self.data[self.front]
        

    def Rear(self): # T(n): O(1)
        return -1 if self.isEmpty() else self.data[self.rear]
        

    def isEmpty(self):
        return True if self.front==-1 and self.rear==-1 else False
        

    def isFull(self):
        return True if (self.rear+1)%self.n == self.front else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()