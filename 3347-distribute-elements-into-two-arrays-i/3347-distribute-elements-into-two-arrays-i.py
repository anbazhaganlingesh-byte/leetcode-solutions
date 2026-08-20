class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        l=[nums[0]]
        r=[nums[1]]
        for i in range(2,len(nums)):
            if l[-1]>r[-1]:
                l.append(nums[i])
            else:
                r.append(nums[i])
        return l+r
