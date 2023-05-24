def graph_coloring(graph, num_of_colors):
    num_vertices = len(graph)
    colors = [0] * num_vertices

    def is_safe(vertex, color):
        for i in range(num_vertices):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True

    def graph_coloring_util(vertex):
        if vertex == num_vertices:
            return True

        for color in range(1, num_of_colors + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                if graph_coloring_util(vertex + 1):
                    return True
                colors[vertex] = 0

    if not graph_coloring_util(0):
        print("No solution exists.")
    else:
        print("Graph coloring solution:")
        for i in range(num_vertices):
            print(f"Vertex {i}: Color {colors[i]}")


# Example usage
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
num_of_colors = 3
graph_coloring(graph, num_of_colors)
