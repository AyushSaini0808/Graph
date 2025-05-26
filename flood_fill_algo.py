'''
Q.
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
'''

'''
A. Basically we start performing BFS starting from the source position and change all
the cells that have the same initial color to the updated color.

'''

image = [[1,1,1],[1,1,0],[1,0,1]]
ROWS=len(image)
COLS=len(image[0])

visited=set() # contains elements (r,c)

def bfs(r,c,color):
    visited.add((r,c))
    prev_color=image[r][c]
    image[r][c]=color
    q=[]
    q.append((r,c))
    while q:
        row,col=q.pop(0)
        combinations=[[1,0],[0,1],[-1,0],[0,-1]]
        for dr,dc in combinations:
            R,C=row+dr,col+dc
            if ((R,C) not in visited) and (R in range(ROWS)) and (C in range(COLS)) and (image[R][C]==prev_color):
                # Set the color at that valid position to the new color
                image[R][C]=color
                # Add that cell as visited
                visited.add((R,C))
                # Append it to the queue
                q.append((R,C))

def main():
    sr,sc,color=1,1,2
    bfs(sr,sc,color)
    print(image)

if __name__=="__main__":
    main()
