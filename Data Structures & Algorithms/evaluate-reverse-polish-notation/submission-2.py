import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        osszeg=0
        for i in tokens:
            if i=="+":
                for i in range(2):
                    a=stack.pop()
                    osszeg+=a
                stack.append(osszeg)
                osszeg=0
                

            elif i=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)

            elif i=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(b*a)
            elif i=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack.pop()
                