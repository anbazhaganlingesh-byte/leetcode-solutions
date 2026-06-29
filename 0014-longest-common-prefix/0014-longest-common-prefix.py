class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength=len(strs[0])
        for i in range(len(strs)):
            if minlength>len(strs[i]):
                minlength=len(strs[i])
        
        ans=""
        if len(strs)==1:
            return strs[0]
        for i in range(minlength):
            f=True
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    f=False
            if f:
                ans+=strs[j][i]
            else:
                break
        return ans