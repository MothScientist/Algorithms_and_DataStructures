class DirectedGraph:
    def __init__(self):
        # We use a dictionary to store the graph.
        # Dictionary keys are vertices and values are another dictionary with edges and their weights for each vertex
        self.graph = {}

    def add_vertex(self, node):
        # Adding a vertex to the graph.
        # If the vertex is not yet in the graph, we create an empty dictionary for its edges.
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, src_node, dest_node, weight):
        # We add an edge between the vertices src_vertex and dest_vertex with weight.
        # If there are no vertices in the graph yet, add them.
        self.add_vertex(src_node)
        self.add_vertex(dest_node)
        self.graph[src_node][dest_node] = weight

    def get_edges(self, node):  # Returns (vertex, weight) pairs for all edges coming from a vertex.
        return [(dest_vertex, self.graph[node][dest_vertex]) for dest_vertex in self.graph[node]]

    def __str__(self):  # Returns a string representation of the graph.
        result = []
        for vertex in sorted(self.graph.keys()):
            edges_str = ', '.join([f"{dest_vertex}({weight})" for dest_vertex, weight in self.graph[vertex].items()])
            result.append(f"{vertex}: {edges_str}")
        return "\n".join(result)

    def dijkstras_algorithm(self, start_node, finish_node):
        if start_node not in self.graph.keys():
            raise Exception("Invalid start node")

        if finish_node not in self.graph.keys():
            raise Exception("Invalid end node")

        unvisited_nodes = set(self.graph.keys())
        shortest_path = {}
        previous_nodes = {}
        max_value = float('inf')

        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = self.graph[current_min_node].keys()
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.graph[current_min_node][neighbor]
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)

        return shortest_path.get(finish_node)

    def greedy_coloring(self, start_node: str):
        # Create a dictionary where we will store the colors of the vertices.
        colors = {}
        mincolors = {i for i in range(len(self.graph))}

        visited = [start_node]
        to_explore = [start_node]

        # Depth-first search.
        while to_explore:
            node = to_explore.pop()
            neighbors = list(self.graph[node].keys())

            # Since our graph can be directed, we need to check the vertices for which the current vertex is a neighbor.
            for side_node in self.graph.keys():
                if node in list(self.graph[side_node].keys()) and side_node not in neighbors:
                    neighbors.append(side_node)

            # Get the colors used by neighboring vertices.
            neighbors_colors = {colors[neighbor] for neighbor in neighbors if neighbor in colors}

            # Select the minimum color that is not used by the neighbors.
            colors[node] = min(mincolors.difference(neighbors_colors))

            for i in neighbors:
                if i not in visited:
                    to_explore.extend(i)
                    visited.append(i)

        return colors

    def get_chromatic_number(self):
        chromatic_numbers = []
        # We will alternately color the graph, each time choosing a different vertex as the first one.
        for node in self.graph.keys():
            chromatic_numbers.append(max(self.greedy_coloring(node).values()))
        return min(chromatic_numbers) + 1


# Examples of using
g = DirectedGraph()

g.add_edge('A', 'L', 20)
g.add_edge('A', 'B', 3)
g.add_edge('A', 'E', 5)
g.add_edge('A', 'G', 8)

g.add_edge('B', 'A', 3)
g.add_edge('B', 'D', 6)
g.add_edge('B', 'P', 26)
g.add_edge('B', 'T', 2)

g.add_edge('D', 'B', 6)
g.add_edge('D', 'E', 8)
g.add_edge('D', 'M', 4)
g.add_edge('D', 'N', 13)
g.add_edge('D', 'Q', 6)

g.add_edge('E', 'D', 1)
g.add_edge('E', 'J', 7)
g.add_edge('E', 'H', 19)

g.add_edge('F', 'N', 15)
g.add_edge('F', 'U', 16)

g.add_edge('G', 'A', 8)
g.add_edge('G', 'E', 10)
g.add_edge('G', 'K', 8)

g.add_edge('H', 'O', 10)
g.add_edge('H', 'J', 7)

g.add_edge('I', 'L', 13)
g.add_edge('I', 'G', 7)

g.add_edge('J', 'G', 8)
g.add_edge('J', 'M', 17)
g.add_edge('J', 'H', 7)
g.add_edge('J', 'R', 6)

g.add_edge('K', 'I', 20)
g.add_edge('K', 'G', 8)

g.add_edge('L', 'I', 13)
g.add_edge('L', 'P', 1)

g.add_edge('M', 'D', 4)
g.add_edge('M', 'F', 13)
g.add_edge('M', 'O', 19)

g.add_edge('N', 'C', 7)
g.add_edge('N', 'D', 13)

g.add_edge('O', 'M', 19)
g.add_edge('O', 'U', 4)

g.add_edge('P', 'A', 4)

g.add_edge('Q', 'T', 5)
g.add_edge('Q', 'C', 11)

g.add_edge('R', 'K', 12)
g.add_edge('R', 'J', 4)

g.add_edge('S', 'V', 1)

g.add_edge('U', 'F', 12)

g.add_edge('V', 'W', 4)
g.add_edge('V', 'S', 2)

g.add_edge('W', 'S', 5)

# print(g.graph)  # Will output the graph as a list of edges and their weights
#
# print(g.dijkstras_algorithm('U', 'L'))
#
# print(g.greedy_coloring('A'))
#
# print(g.get_chromatic_number())
