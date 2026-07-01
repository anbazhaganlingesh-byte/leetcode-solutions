class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        queue = []
        front = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while front < len(queue):
            x, y = queue[front]
            front += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        heap = []
        def push(item):
            heap.append(item)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[p][0] >= heap[i][0]:
                    break
                heap[p], heap[i] = heap[i], heap[p]
                i = p
        def pop():
            if len(heap) == 1:
                return heap.pop()
            top = heap[0]
            heap[0] = heap.pop()
            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < len(heap) and heap[left][0] > heap[largest][0]:
                    largest = left
                if right < len(heap) and heap[right][0] > heap[largest][0]:
                    largest = right
                if largest == i:
                    break
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
            return top
        visited = [[False] * n for _ in range(n)]
        push((dist[0][0], 0, 0))
        while heap:
            safe, x, y = pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n - 1 and y == n - 1:
                return safe
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    push((min(safe, dist[nx][ny]), nx, ny))
        return 0