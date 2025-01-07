from collections import deque


def bfs(graph, start):
    # Create a queue for BFS
    queue = deque([start])
    # A set to keep track of visited nodes
    visited = set()
    visited.add(start)  # Mark the starting node as visited
    while queue:
        # Dequeue a vertex from the queue
        current = queue.popleft()
        print(current, end=" ")  # Process the current node
        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[current]:
            vertex = neighbor[0]
            if vertex not in visited:
                # If a vertex has not been visited, mark it visited and enqueue it
                visited.add(vertex)
                queue.append(vertex)


def dfs_recursive(graph, node, visited):
    visited.add(node)  # Mark the current node as visited
    print(node, end=" ")  # Process the current node
    for neighbor in graph[node]:
        vertex = neighbor[0]
        if vertex not in visited:
            dfs_recursive(graph, vertex, visited)


def add_edge_adj_matrix(mat, i, j, weight=1):
    # Add an edge between two vertices
    mat[i][j] = weight  # Graph is
    mat[j][i] = weight  # Undirected


def display_adj_matrix(mat):
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))


def add_edge_adj_list(adj_list, u, v, weight=1):
    """
    Add an edge between vertex u and v with the given weight.
    """
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append((v, weight))
    adj_list[v].append((u, weight))  # For undirected graph


def display_adj_list(adj):
    for x, y in adj.items():
        print(x, ":", y)


if __name__ == "__main__":
    V = 4  # Number of vertices
    mat = [[0] * V for _ in range(V)]
    # Add edges to the graph
    add_edge_adj_matrix(mat, 0, 1)
    add_edge_adj_matrix(mat, 0, 2)
    add_edge_adj_matrix(mat, 1, 2)
    add_edge_adj_matrix(mat, 2, 3)
    # Optionally, initialize matrix directly
    """
    mat = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    """
    # Display adjacency matrix
    print("Adjacency Matrix:")
    display_adj_matrix(mat)

    # Create a graph with 4 vertices and no edges
    adj = {}
    # Now add edges one by one
    add_edge_adj_list(adj, 0, 1)
    add_edge_adj_list(adj, 0, 2)
    add_edge_adj_list(adj, 1, 2)
    add_edge_adj_list(adj, 2, 3)
    add_edge_adj_list(adj, 3, 1)
    add_edge_adj_list(adj, 3, 0)
    print("Adjacency List Representation:")
    display_adj_list(adj)

    print("Breadth-First Search starting from node A:")
    bfs(adj, 0)
    print("\nDepth-First Search starting from node A:")
    visited = set()
    dfs_recursive(adj, 0, visited)
    print("\n")
