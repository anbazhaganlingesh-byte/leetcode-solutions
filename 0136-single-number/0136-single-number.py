class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        s2=sum(set(nums))
        return (2*s2-s)