class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        curr_count = 0

        def dfs(r, c):
            nonlocal area
            nonlocal curr_count
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 
            
            if grid[r][c] == 1:
                curr_count += 1
                area = max(area, curr_count)
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_count = 0
                    dfs(r, c)
                
        return area

        
        



        