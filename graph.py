'''
Representation and traversal techniques of graph 
Suppose that we have a graph with 5 nodes and 6 edges as 1-2,1-3,2-4,3-5,4-5,3-4

The task is to represent the graph in the form of adjacency matrix and adjacency list.
We are also supposed to implement Bread-First-Search(BFS) and Depth-First-Search(DFS) techniques
'''
from collections import deque
def adj_matrix_rep(n,edges):
    adj_matrix=[[0]*(n+1) for _ in range(n+1)]
    for i in edges:
        adj_matrix[i[0]][i[1]]=adj_matrix[i[1]][i[0]]=1
    return adj_matrix
    
def adj_list_rep(edges,n):
    adj_list={}
    for i in range(n+1):
        adj_list[i]=[]
    for node1,node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    return adj_list
    
def bfs(graph,start):
    q=deque([start])
    visited=set([start])
    while q:
        child=q.popleft()
        print(child,end="->")
        for neighbor in graph[child]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    

def dfs(graph,node,visited):
    visited.add(node)
    print(node,end="->")
    for i in graph[node]:
        if i not in visited:
            dfs(graph,i,visited)
        

  
def main():
    print("Enter the number of nodes and edges present in the graph: ")
    n,m=map(int,input().split())
    edges=[]
    for _ in range(m):
        print("Enter the edge in the following format (n1,n2):")
        n1,n2=map(int,input().split())
        if n1<=n and n2<=n and n1>0 and n2>0:
            edges.append([n1,n2])
        else:
            print("Node value cannot be greater than the maximum value provided or less than 0")
    print("*** Adjacency Matrix Representation of the Graph ***")
    print(adj_matrix_rep(n,edges))
    
    print("*** Adjacency List Representation of the Graph ***")
    graph=adj_list_rep(edges,n)
    print(graph)
    
    root=int(input("Enter the node to start the traversal from :"))
    print("*** Breadth First Search for given graph ***")
    bfs(graph,root)
    print("\n*** Depth First Search for given graph ***")
    dfs(graph,root,set())
        
    
if __name__=="__main__":
    main()
