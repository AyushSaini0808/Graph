'''
Q.
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

'''
A.

'''
grid = [[2,1,1],[1,1,0],[0,1,1]]
# Obtaining the total no. of rows and columns
ROWS=len(grid)
COLS=len(grid[0])
directions=[[1,0],[-1,0],[0,1],[0,-1]]
def main(grid):
    fresh=0
    mins=0
    q=[]
    # Identifying the number of fresh oranges and appending all rotten orange positions in the queue
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c]==1:
                fresh+=1
            elif grid[r][c]==2:
                q.append((r,c))
    # Run BFS until q is not empty or there arent any fresh oranges
    while q and fresh:
        for i in range(len(q)):
            R,C=q.pop(0)
            for dr,dc in directions:
                r=R+dr
                c=C+dc
                if ((r not in range(ROWS)) or (c not in range(COLS)) or (grid[r][c]!=1)):
                    continue
                grid[r][c]=2
                q.append((r,c))
                fresh-=1
        mins+=1
    
    return mins if fresh==0 else -1
        
if __name__=="__main__":
    print(main(grid))