class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=len(nums)+1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1