class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.strip()
        a=a.split()
        m=""
        for i in range(len(a)-1,0,-1):
            m+=a[i]+" " 
        m+=a[0]
        return m