class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m,c=k,0
        if len(blocks)<k:
            return -1
        else:
            for i in range(k):
                if blocks[i]=="W":
                    c+=1
            m=min(m,c)
            for i in range(k,len(blocks)):
                if blocks[i-k]=="W":
                    c-=1
                if blocks[i]=="W":
                    c+=1
                m=min(c,m)
            return m
