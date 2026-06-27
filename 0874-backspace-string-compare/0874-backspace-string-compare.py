class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stack2=[]
        for i in s:
            if i=="#":
                if stack:
                    stack.pop()
                continue
            
            stack.append(i)
        for i in t:
            if i=="#":
                if stack2:
                    stack2.pop()
                continue
            stack2.append(i)
        if stack==stack2:
            return True
        else:
            return False
            