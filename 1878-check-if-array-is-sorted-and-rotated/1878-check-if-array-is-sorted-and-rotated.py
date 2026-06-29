class Solution:
    def check(self, nums: List[int]) -> bool:
        sarr=sorted(nums)
        f=False
        if nums==sarr:
            return True
        else:
            for i in range(len(nums)):
                if nums[i:]+nums[:i]==sarr:
                    f=True
            return f