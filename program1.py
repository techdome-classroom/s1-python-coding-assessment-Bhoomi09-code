class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
          def num_islands(grid):
    if not grid:
        return 0
 
    def dfs(grid, i, j):
        # If out of bounds or water, return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return
        # Mark the current land as visited by turning it into water
        grid[i][j] = 'W'
        # Visit all 4 adjacent cells (up, down, left, right)
        dfs(grid, i - 1, j)  # up
        dfs(grid, i + 1, j)  # down
        dfs(grid, i, j - 1)  # left
        dfs(grid, i, j + 1)  # right
 
    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':  # Found a piece of unvisited land
                dfs(grid, i, j)    # Start exploring this island
                island_count += 1  # Increase the island count
 
    return island_count          
        
