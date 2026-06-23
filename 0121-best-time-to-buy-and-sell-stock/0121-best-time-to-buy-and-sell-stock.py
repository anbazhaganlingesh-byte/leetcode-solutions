class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        c=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<c:
                c=prices[i]
            elif prices[i]-c>s:
                s=prices[i]-c
        return s