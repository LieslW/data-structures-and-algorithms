from data_structures.queue import Queue


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []

        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)

        if end_vertex not in self.adjacency_list:
            raise KeyError()
        self.adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self, vertex):
        all_vertices = []
        breadth = Queue()
        visited_vertices = set()
        breadth.enqueue(vertex)
        visited_vertices.add(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            all_vertices.append(front.value)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited_vertices:
                    visited_vertices.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)
        return all_vertices

    def depth_first_search(self, vertex):
        if self.adjacency_list == {}:
            return []

        def traverse(node):
            list.append(node.value)
            neighbors = self.get_neighbors(node)

            for edge in neighbors:
                if edge.vertex.visited == 0:
                    edge.vertex.visited = 1
                    node.visited = 1
                    traverse(edge.vertex)

        list = []
        traverse(vertex)
        return list

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    # what would happen if we called get_neighbors with a vertex that isn't in the graph?


class Vertex:
    def __init__(self, value, visited=0):
        self.value = value
        self.visited = visited


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
