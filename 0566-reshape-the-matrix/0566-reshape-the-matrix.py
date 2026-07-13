class Solution(object):
    def matrixReshape(self, mat, r, c):
        if not mat: 
            return mat
        if len(mat) * len(mat[0]) != r * c:
            return mat
        ans=[[0 for i in range(c)] for i in range(r)]
        inx=0
        while inx<r*c:
            ans[inx//c][inx%c]=mat[inx//len(mat[0])][inx%len(mat[0])]
            inx+=1
        return ans  