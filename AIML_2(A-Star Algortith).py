graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D' : 3, 'E' : 1},
    'C': {'F' : 5},
    'D': {},
    'E': {'F': 2},
    'F': {}
    }
heuristic = {
    'A':5,
    'B':4,
    'C':2,
    'D':6,
    'E':2,
    'F':0
}
def a_star(start, goal):
    open_list=[start]
    cost = {start:0}

    while open_list:
      current = open_list[0]

      for node in open_list:
        if cost[node] + heuristic[node] < cost[current] + heuristic[current]:
         current = node

      if current == goal:
        print("Goal Reached")
        print("Cost =", cost[current])
        return

      open_list.remove(current)

      for neighbor in graph[current]:
        new_cost = cost[current] + graph[current][neighbor]

        if neighbor not in cost:
          cost[neighbor] = new_cost
          open_list.append(neighbor)

a_star('A', 'F')