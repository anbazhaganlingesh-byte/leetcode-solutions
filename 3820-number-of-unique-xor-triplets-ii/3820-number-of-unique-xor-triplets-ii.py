class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s=set(nums)
        ans=set()
        sub=set()
        for i in s:
            for j in s:
                sub.add(i^j)
        for i in sub:
            for j in s:
                ans.add(i^j)
        print(ans)
        return len(ans)