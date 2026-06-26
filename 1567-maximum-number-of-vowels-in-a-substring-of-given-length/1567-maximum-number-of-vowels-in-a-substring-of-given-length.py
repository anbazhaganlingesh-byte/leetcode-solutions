class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i,j=0,0
        a="aeiou"
        c,m=0,0
        for i in range(k):
            if s[i]in a:
                c+=1
        m=c
        for i in range(k,len(s)):
            if s[i-k] in a:
                c-=1
            if s[i] in a:
                c+=1
            m=max(m,c)
        return m