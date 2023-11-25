class KthLargest(object):
    # By converting it to min h of size k, T(n): O((n-k)*logn), S(n)-O(n)- heap
    def __init__(self, k, nums):
        self.minH,self.k = nums,k
        heapq.heapify(self.minH) # Converts it to min heap
        # Kth largest ele is at the Parent Node

        while len(self.minH)>self.k: # O((n-k).logn)
            heapq.heappop(self.minH)

    def add(self, val):
        heapq.heappush(self.minH,val)
        if len(self.minH)>self.k: # O(logn)
            heapq.heappop(self.minH)
        return self.minH[0]
    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)