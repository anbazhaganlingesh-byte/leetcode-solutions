class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]
        score[0][0] = 0
        ways[0][0] = 1
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X' or (i == 0 and j == 0):
                    continue
                for x, y in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                    if x >= 0 and y >= 0 and score[x][y] != -1:
                        cur = score[x][y]
                        if cur > score[i][j]:
                            score[i][j] = cur
                            ways[i][j] = ways[x][y]
                        elif cur == score[i][j]:
                            ways[i][j] = (ways[i][j] + ways[x][y]) % MOD
                if score[i][j] != -1 and board[i][j].isdigit():
                    score[i][j] += int(board[i][j])
        if score[-1][-1] == -1:
            return [0, 0]
        return [score[-1][-1], ways[-1][-1]]