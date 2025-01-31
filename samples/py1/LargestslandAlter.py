#You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#Return the size of the largest island in grid after applying this operation.
#An island is a 4-directionally connected group of 1s.

class Solution:
    def __init__(self, grid:list[list[int]]) -> int:
        self.grid=grid
        self.area=0
        self.ROWS=len(self.grid)
        self.COLS =len(self.grid[0])
       

    def IslandMeasure(self, grid_m):

        visit = set()

        def dfs(r,c):
            if (r <0 or r == self.ROWS or c <0 or c == self.COLS or
            grid_m[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            # dfs on 4 sides to hit water
            return ( 
                1 + dfs(r +1, c) +
                dfs(r - 1, c) +
                dfs(r, c +1) +
                dfs(r, c-1) 
                )
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.area=max(self.area, dfs(r,c))
        return(self.area)
    
    def AlterGridMeasure(self):
        self.area_alt=0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j]==0:
                    grid__ = [row[:] for row in self.grid]
                    grid__[i][j]=1
                    self.area_alt=max(self.area_alt,self.IslandMeasure(grid__) )
                else:
                    self.area_alt=max(self.area_alt,self.IslandMeasure(self.grid) )

        return(self.area_alt)


def main():
    grid1= [[0,1], [0,1]]
    grid2=[[1,1],[1,0]]
    grid3=[[1,1],[1,1]]
    grid4=[[1,0,1],[0,0,0],[0,1,1]]

    #Instantiate Class
    sln1=Solution(grid1)
    sln2=Solution(grid2)
    sln3=Solution(grid3)
    sln4=Solution(grid4)
    #Process Instance1
    print(sln1.AlterGridMeasure()) #3
    print(sln2.AlterGridMeasure()) #4
    print(sln3.AlterGridMeasure()) #4
    print(sln4.AlterGridMeasure()) #11

if __name__=='__main__':
    main()