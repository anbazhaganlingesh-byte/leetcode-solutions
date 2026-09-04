class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        suff=[0]*n
        mn=float('inf')
        for i in range(n-1,-1,-1):
            mn=min(mn,nums[i])
            suff[i]=mn
        mx=0
        for i in range(n):
            mx=max(mx,nums[i])
            sr=mx-suff[i]
            if sr<=k:
                return i
        return -1