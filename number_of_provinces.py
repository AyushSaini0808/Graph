'''
Q.There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside 
of the group.You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the 
ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

'''
A. So basically the problem requires us to find the totla number of connected components, where 
basically every component contains the connected cities. 
Firstly, we need to convert the matrix(adj_matrix) into an adjacency list.
Next, we would be iterating through 0....n+1 nodes to determine whether the given node is 
visited or not. If it's not visited we can start the dfs from this node and mark all the 
nodes in that connected component to make up a province. 
'''

def convert_matrix_to_list(isConnected):
    adj_list={}
    for i in range(len(isConnected)):
        adj_list[i]=[]
    for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
            if isConnected[i][j]==1 and i!=j:
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list
                
def dfs(graph,node,visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

def main():
    count=0
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    graph=convert_matrix_to_list(isConnected)
    visited=set()
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(graph,i,visited)
            count+=1
    print(f"Number of provinces are: {count}")

if __name__=="__main__":
    main()
        
        