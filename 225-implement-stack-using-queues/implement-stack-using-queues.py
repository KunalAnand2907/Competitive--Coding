class MyStack(object):

    def __init__(self):
        self.q = deque() # double ended q
        

    def push(self, x):
        self.q.append(x) # sim as queue at the rear end
        

    def pop(self):#[1,2] - O(n)
        return self.q.pop()

    def top(self):
        return self.q[-1]
        

    def empty(self):
        return len(self.q)==0 # if empty ret True else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()