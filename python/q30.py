'''30. Write a program to detect cycles in a directed graph using Depth-First Search (DFS).'''

def is_cyc_util(adj, u, visited, rec_stack): 
    if not visited[u]:    
        # Mark the current node as visited and part of recursion stack
        visited[u] = True
        rec_stack[u] = True
        # Recursion for all the adjacent vertices 
        for x in adj[u]:
            if not visited[x] and is_cyc_util(adj, x, visited, rec_stack):
                return True
            elif rec_stack[x]:
                return True
    # Remove the vertex from recursion stack
    rec_stack[u] = False
    return False

def is_cyclic(adj, V):
    visited = [False] * V
    rec_stack = [False] * V
    # Recursion to detect cycle in different DFS trees
    for i in range(V):
        if not visited[i] and is_cyc_util(adj, i, visited, rec_stack):
            return True
    return False

if __name__ == "__main__":
    V = 4
    adj = [[] for _ in range(V)]

    # graph construction
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(3)

    if is_cyclic(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")
