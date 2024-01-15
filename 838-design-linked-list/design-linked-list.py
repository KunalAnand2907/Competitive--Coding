class Node(object):
     def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.l=0
        
    def get(self, index):
        # index=0 so if we have 1 2 length is 2 and at 2 we need to get the index--not posible
        if index>=self.l or index<0: # out of bounds index
            return -1
        temp=self.head
        while(index>0):
            temp=temp.next
            index-=1
        return temp.val # simply return if index=0

    def addAtHead(self, val):
        new_node =  Node(val)
        new_node.next=self.head
        self.head=new_node
        self.l+=1

    def addAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
        new_node.next=None
        self.l+=1
        
    def addAtIndex(self, index, val):
        if index>self.l or index<0:
            return -1
        if(index == 0):
            new_node=Node(val)
            new_node.next=self.head
            self.head=new_node
        else:
            new_node=Node(val)
            temp=self.head
            for i in range(0,index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.l+=1
        
    def deleteAtIndex(self, index):
        if index>=self.l or index<0:
            return -1
        if index==0:
            self.head=self.head.next
        else:
            temp=self.head
            prev=None
            for i in range(0,index):
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp.next=None
        self.l-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)