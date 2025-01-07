from collections import deque


def detect_cycle_in_disconnected_graph(graph):
    visited = set()  # Keep track of all visited nodes globally
    for node in graph:  # Iterate over all nodes to cover disconnected components
        if node not in visited:
            # print(detect_cycle_dfs(graph, node, visited, -1))
            if detect_cycle_bfs(graph, node, visited):
                return True
    return False

def detect_cycle_dfs(adj, current, visited, parent):
    # Mark the current node as visited
    visited.add(current)
    # Recur for all the vertices adjacent to this vertex
    for neighbor in adj[current]:
        # If an adjacent vertex is not visited,
        # then recur for that adjacent
        if neighbor[0] not in visited:
            if detect_cycle_dfs(adj, neighbor[0], visited, current):
                return True
        # If an adjacent vertex is visited and
        # is not the parent of the current vertex,
        # then there exists a cycle in the graph.
        elif neighbor[0] != parent:
            return True
    return False

def detect_cycle_bfs(graph, start, visited):
    # Create a queue for BFS
    queue = deque([start])
    visited.add(start)  # Mark the starting node as visited
    parent = {}
    parent[start] = -1  # Initialize the parent of the start node
    while queue:
        # Dequeue a vertex from the queue
        current = queue.popleft()
        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[current]:
            vertex = neighbor[0]
            if vertex not in visited:
                # If a vertex has not been visited, mark it visited and enqueue it
                visited.add(vertex)
                queue.append(vertex)
                parent[vertex] = current
            elif vertex in visited and vertex != parent[current]:  # Cycle detected
                return True
    return False


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
    # Create a graph with multiple disconnected components
    adj = {}
    # Component 1
    add_edge_adj_list(adj, 0, 1)
    add_edge_adj_list(adj, 0, 2)
    add_edge_adj_list(adj, 1, 2)
    # Component 2
    add_edge_adj_list(adj, 3, 4)
    # Component 3
    add_edge_adj_list(adj, 5, 6)

    print("Adjacency List Representation:")
    display_adj_list(adj)
    print("Cycle present in graph:", detect_cycle_in_disconnected_graph(adj))
