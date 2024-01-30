class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
           # With stack traverse from L-R
           stack =[]
           for c in tokens:
               if c == "+":
                   stack.append(stack.pop() + stack.pop())
               elif c == "-":
                   a,b = stack.pop(), stack.pop()
                   stack.append(b-a)
               elif c == "*":
                   stack.append(stack.pop() * stack.pop())
               elif c == "/":
                   a,b = stack.pop(), stack.pop()
                   stack.append(int(b/a))
               else: # operand found
                   stack.append(int(c))
           return stack[0]