'''
Q. Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two cells sharing a common edge is 1.

A. To solve this problem, first we need to identify all the 0's in the given matrix and 
add them all to the queue, next we set all the 1's to -1. Now, we begin with the BFS
popping the first (R,C) from the queue. Check if its neighbors are -1 , if it is then 
then we set mat[r][c] ( the neighbor of the current node ) = mat[R][C] (current node) + 1.
Return mat at end
'''
mat = [[0,0,0],[0,1,0],[1,1,1]]
ROWS=len(mat)
COLS=len(mat[0])
directions=[[-1,0],[1,0],[0,1],[0,-1]]
def main():
    q=[]
    for r in range(ROWS):
        for c in range(COLS):
            if mat[r][c]==0:
                q.append((r,c))
            else:
                mat[r][c]=-1
    # Start with the bfs
    while q:
        row,col=q.pop(0)
        for dr,dc in directions :
            R,C=row+dr,col+dc
            if ((R in range(ROWS)) and (C in range(COLS)) and mat[R][C]==-1):
                mat[R][C]=mat[row][col]+1
                q.append((R,C))
                
    return mat
    
    
if __name__=="__main__":
    print(main())
    