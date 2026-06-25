class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s=su=0
        s1=defaultdict(int)
        if len(nums)<k:
            return 0
        for i in range(k):
            s1[nums[i]]+=1
            s+=nums[i]
        if len(s1)==k:
            su=s
        for i in range(k,len(nums)):
            l=i-k
            s1[nums[l]]-=1
            s-=nums[l]
            if s1[nums[l]]==0:
                del s1[nums[l]]
            s1[nums[i]]+=1
            s+=nums[i]
            if len(s1)==k:
                su=max(su,s)
        return su
