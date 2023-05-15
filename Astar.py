# Define the heuristic and graph
heuristic = {'A': 4, 'B': 6, 'C': 1, 'D': 2, 'E': 3}

graph = {
    'A': {'B': 1, 'C': 1},
    'B': {},
    'C': {},
    'D': {},
    'E': {}
}

# Define the start and goal nodes
start_node = 'A'
goal_node = 'C'

def a_star(start, goal, heuristic, graph):
    # Initialize the priority queue with the start node
    queue = [(heuristic[start], [start], 0)]
    
    while queue:
        # Get the node with the lowest cost
        (cost, path, gn) = queue.pop(0)
        current = path[-1]
        
        # If we've reached the goal node, return the path
        if current == goal:
            return (path, gn)
        
        # Expand the current node's neighbors
        for neighbor, cost in graph[current].items():
            new_path = path + [neighbor]
            hn = heuristic[neighbor]
            fn = gn + cost + hn
            queue.append((fn, new_path, gn + cost))
        
        # Sort the queue by lowest cost
        queue.sort()
    
    # If we've exhausted the queue without reaching the goal, there is no path
    return None

# Call the A* algorithm and print the result
result = a_star(start_node, goal_node, heuristic, graph)

if result:
    path, cost = result
    print(f"The A* path with total cost {cost} is: {', '.join(path)}")
else:
    print("No path found")
