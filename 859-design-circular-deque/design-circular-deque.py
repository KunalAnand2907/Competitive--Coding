class MyCircularDeque(object):

    def __init__(self, k):
        self.items=[] # Inirialize empty DeQue
        self.k=k # maximum size of DeQue
        

    def insertFront(self, value):
        if(self.isFull()):
            return False
        else:
            self.items.insert(0,value)
            return True
        
    def insertLast(self, value):
        if(self.isFull()):
            return False
        else:
            self.items.append(value)
            return True
        
    def deleteFront(self):
        if(self.isEmpty()):
            return False
        else:
            self.items.pop(0)
            return True
        
    def deleteLast(self):
        if(self.isEmpty()):
            return False
        else:
            self.items.pop()
            return True
        

    def getFront(self):
        if len(self.items)==0:
            return -1
        else:
            return self.items[0]
        
        
    def getRear(self):
        if len(self.items)==0:
            return -1
        else:
            return self.items[len(self.items)-1]
        
        
    def isEmpty(self):
        return self.items==[]
        
        

    def isFull(self):
        return len(self.items)==self.k
        
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()