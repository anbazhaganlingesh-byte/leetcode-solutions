from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=defaultdict(int)
        p=defaultdict(int)
        z=0
        for num in nums:
            if num < 0:
                n[num]+=1
            elif num > 0:
                p[num]+=1
            else:
                z+=1
        
        res=[]
        if z:
            for i in n:
                if -i in p:
                    res.append((0, i, -i))       
            if z>2:
                res.append((0,0,0))

        for set1, set2 in ((n,p), (p, n)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            res.append((j, j2, -j-j2))
        return res