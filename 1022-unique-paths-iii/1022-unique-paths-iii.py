class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        c=0
        a=0
        s,e=0,0
        n=len(grid)
        m=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    s=i
                    e=j
                if grid[i][j]==-1:
                    a+=1
        sol=[[0]*m for _ in range(n)]
        def back(i,j,step):
            nonlocal c
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==-1 or sol[i][j]==1:
                return False
            if grid[i][j]==2:
                if  step==d:
                    c+=1
                return False
            sol[i][j]=1
            if back(i+1,j,step+1):
                return True
            if back(i,j+1,step+1):
                return True
            if back(i,j-1,step+1):
                return True
            if back(i-1,j,step+1):
                return True
            sol[i][j]=0
            return False
        d=n*m-a
        back(s,e,1)
        return c