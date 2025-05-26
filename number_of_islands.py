'''
Q.
Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.An island is surrounded by water and is formed
by connecting adjacent lands horizontally or vertically. You may assume all four edges
of the grid are all surrounded by water.
'''

'''
A. Starting from the first value that appears as 1 we would start finding other 1's surrounding 
or near than particular 1 ( essentially obtaining the component). So that at the end we would
essentially be computing the number of connected components. 
We would be performing BFS on the grid with a twist on how we would find the 'neighbors' of a 
particular node ( the given value at that row and column).

'''

# Obtaining the number of rows and columns
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
ROWS=len(grid)
COLS=len(grid[0])
    
visited=set()

# Creating the traversal function
def bfs(r,c):
    q=[]
    q.append((r,c))
    visited.add((r,c))
    while q:
        R,C=q.pop(0)
        combinations=[[1,0],[-1,0],[0,1],[0,-1]]
        for dr,dc in combinations:
            row,col=R+dr,C+dc
            if (row in range(ROWS)) and (col in range(COLS)) and ((row,col) not in visited) and (grid[row][col]=="1"):
                visited.add((row,col))
                q.append((row,col))

def main():
    islands=0
    for r in range(ROWS):
        for c in range(COLS):
            if (grid[r][c] == "1") and ((r,c) not in visited):
                # One bfs search means one island has been formed
                bfs(r,c)
                islands+=1
    print(f"Number of islands: {islands}")
    
    
if __name__=="__main__":
    main()