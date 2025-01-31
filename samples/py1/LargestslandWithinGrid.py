#Python Island Grid 
#m by n island grid binary data
#find maxiumum area of any island within the entire grid

class Solution:
    def __init__(self, grid:list[list[int]]) -> int:
        self.grid=grid
        self.area=0

    def largestIsland(self): #: list[list[int]]) -> int:
        ROWS, COLS =len(self.grid), len(self.grid[0])
        visit = set()

        def dfs(r,c):
            if (r <0 or r == ROWS or c <0 or c == COLS or
            self.grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            # dfs on 4 sides to hit water
            return ( 
                1 + dfs(r +1, c) +
                dfs(r - 1, c) +
                dfs(r, c +1) +
                dfs(r, c-1) 
                )
        
        for r in range(ROWS):
            for c in range(COLS):
                self.area=max(self.area, dfs(r,c))
        return(self.area)
        
    
def main():
    grid= [[1,1,1,0,0],
        [1,1,0,0,0],
        [1,1,0,0,0],
        [1,1,0,1,1],
        [1,1,0,1,1]]

    #Instantiate Class
    sln1=Solution(grid)
    #Process Instance1
    area=sln1.largestIsland()
if __name__=='__main__':
    main()