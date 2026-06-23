class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        a="aeiouAEIOU"
        while(i<j):
            if s[i] not in a and i<j:
                i+=1
                continue
            elif s[j] not in a and i<j:
                j-=1
                continue
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(str(i)for i in s)