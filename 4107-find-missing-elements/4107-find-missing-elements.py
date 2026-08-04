class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        x=[]
        nums.sort()
        c=0
        for i in range(mini,maxi+1):
            if i!=nums[c]:    
                x.append(i)
            else:
                c+=1
        return x