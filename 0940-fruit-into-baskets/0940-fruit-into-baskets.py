class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        fr={}
        ans=0
        for r in range(len(fruits)):
            f=fruits[r]
            fr[f]=fr.get(f,0)+1
            while len(fr) > 2:
                le=fruits[l]
                fr[le]-=1
                if fr[le]==0:
                    del fr[le]
                l+=1
            ans = max(ans,r-l+1)
        return ans
            