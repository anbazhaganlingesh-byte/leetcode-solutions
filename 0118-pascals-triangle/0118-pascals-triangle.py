class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(1, numRows + 1):
            dp.append([0] * i)
        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1
            if i > 0:
                for j in range(1, i):
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp