class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        ans=0
        for i in s:
            c=nums.count(i)
            if m<c:
                m=c
                ans=i
        return ans
        