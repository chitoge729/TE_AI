from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_recursive(start, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Create a graph
graph = Graph()

# Get user input for number of vertices and edges
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Get user input for edges
print("Enter the edges (u, v):")
for _ in range(num_edges):
    u, v = map(int, input().split(','))
    graph.add_edge(u, v)

# Get user input for starting vertex
start_vertex = int(input("Enter the starting vertex: "))

# Perform DFS and BFS
print("Depth First Search (DFS):")
graph.dfs(start_vertex)

print("\nBreadth First Search (BFS):")
graph.bfs(start_vertex)
