class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            subarr=[]
            for j in range(len(matrix)):
                subarr.append(matrix[j][i])
            ans.append(subarr)
        return ans