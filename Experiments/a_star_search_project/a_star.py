import heapq

# Define the graph with neighbors and their edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 7)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic values (estimated cost to reach goal 'G')
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 3,
    'G': 0
}

# A* Search Function
def a_star_search(graph, start, goal, heuristics):
    open_set = []
    heapq.heappush(open_set, (heuristics[start], 0, start, [start]))  # (f, g, node, path)
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g  # Return final path and total cost

        for neighbor, cost in graph.get(current, []):
            new_g = g + cost
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Run the algorithm
start_node = 'A'
goal_node = 'G'
result_path, total_cost = a_star_search(graph, start_node, goal_node, heuristics)

# Output
print("Path found:", " -> ".join(result_path))
print("Total cost:", total_cost)
