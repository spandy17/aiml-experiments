from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': [],
}

def dfs(graph, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            # Add neighbors in reverse order so traversal follows left-to-right
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

# Main Program
start_node = input("Enter Start Node: ").upper()
print("DFS Traversal:")
dfs(graph, start_node)