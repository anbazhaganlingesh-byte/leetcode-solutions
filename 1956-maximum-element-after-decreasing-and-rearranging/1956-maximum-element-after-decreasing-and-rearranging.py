class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi=1
        for i in range(len(arr)):
            if arr[i]>=maxi:
                maxi+=1
        return maxi-1