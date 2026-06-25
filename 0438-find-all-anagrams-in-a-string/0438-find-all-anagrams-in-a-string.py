class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=[]
        s1=p
        s2=s
        if len(s1)>len(s2):
            return []
        s1c=defaultdict(int)
        s2c=defaultdict(int)
        for i in range(len(s1)):
            s1c[s1[i]]+=1
            s2c[s2[i]]+=1
        if s2c==s1c:
            a.append(0)
        for i in range(len(s1),len(s2)):
            left=s2[i-len(s1)]
            s2c[left]-=1
            if s2c[left] == 0:
                del s2c[left]
            s2c[s2[i]]+=1
            if s1c==s2c:
                a.append(i-len(s1)+1)
        return a