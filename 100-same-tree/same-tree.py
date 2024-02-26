# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        #1.) ITERATIVE SOLUTION DFS-STACK- only is we use while loop and pop the element which contains (L,R)
        # stack=[(p,q)]
        # while stack:
        #     p,q=stack.pop()
        #     if p is None and q is None:
        #         continue
        #     if p and q and p.val==q.val:
        #         stack.append((p.left,q.left))
        #         stack.append((p.right,q.right))
        #     else:
        #         return False
        # return True
        # 2.) Recursive Method
        if not(p) and not(q):
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        else:
            return False
              
        
        
        