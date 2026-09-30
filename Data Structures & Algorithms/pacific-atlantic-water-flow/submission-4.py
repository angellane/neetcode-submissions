class Solution:
    #I can also declare directions as a list of sublists with the coords to move in rather than hardcoding the changes 
    #Also can loop through each elements in both sets and add them to a new result list rather than looping through every element in the grid

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        

        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) #top row, everything that is touching pacific
            dfs(rows - 1, c, atl, heights[rows - 1][c]) #bottom row, everything that is touching atlantic

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) #left row, everything touching pacific
            dfs(r, cols - 1, atl, heights[r][cols - 1]) #right row, everything touching atlantic


        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
            
            
        

        


        