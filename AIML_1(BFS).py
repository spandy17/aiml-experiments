from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': [ 'D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}
def bfs (graph, start):
  visited = []
  queue = deque()

  visited.append(start)
  queue.append(start)

  while queue:
    node = queue.popleft()
    print(node,end="")

    for neighbour in graph[node]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

start = input("enter the start node:").upper()
print("BFS Traversal:")
bfs(graph, start)
