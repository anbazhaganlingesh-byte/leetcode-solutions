class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        find=-1
        sind=-1
        while i<=j:
            if nums[i]==target:
                find=i
            else:
                i+=1
            if nums[j]==target:
                sind=j
            else:
                j-=1
            if find>=0 and sind>=0:
                break
        return [find,sind]
