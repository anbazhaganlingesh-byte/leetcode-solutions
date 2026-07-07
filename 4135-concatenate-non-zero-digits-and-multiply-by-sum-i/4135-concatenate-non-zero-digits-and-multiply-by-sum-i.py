class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        st=str(n)
        summ=0
        val=0
        for i in st:
            if int(i)>0:
                val=(val*10)+int(i)
                summ+=int(i)
        return val*summ