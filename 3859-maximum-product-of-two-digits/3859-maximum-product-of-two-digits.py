class Solution:
    def maxProduct(self, n: int) -> int:
        maxi=0
        st=str(n)
        li=[]
        for i in st:
            li.append(int(i))
        li.sort()
        return li[len(li)-1]*li[len(li)-2]