class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        m=[]
        c=0
        for i in nums:
            c+=i
            m.append(c)
        return m