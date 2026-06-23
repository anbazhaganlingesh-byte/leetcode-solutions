class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        m=sum(set(nums))
        return int((m*3-s)/2)