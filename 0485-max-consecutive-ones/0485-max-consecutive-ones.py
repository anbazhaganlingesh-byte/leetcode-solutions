class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=[]
        c=0
        for i in nums:
            if i==1:
                c+=1
            else:
                s.append(c)
                c=0
        s.append(c)
        return max(s)