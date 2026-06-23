class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=[]
        k=0
        for i in nums:
            if i not in a:
                a.append(i)
                nums[k]=i
                k+=1
        return len(a)

