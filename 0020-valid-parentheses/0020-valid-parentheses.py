class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if  i=="{" or i=="(" or i=="[":
                stack.append(i)
            elif i=="]" or i=="}" or i==")":
                if stack==[]:
                    return False
                f=stack.pop()
                if (i==")" and f!="(") or (i=="]" and f!="[") or (i=="}" and f!="{"):
                    return False
        if stack==[]:
            return True
        else:
            return False