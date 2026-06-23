class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        a=numbers
        while i<j:
            if a[i]+a[j]<target:
                i+=1
            elif a[i]+a[j]>target:
                j-=1
            elif a[i]+a[j]==target:
                return i+1,j+1