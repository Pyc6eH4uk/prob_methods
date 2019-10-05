from random import randint
import networkx as nx


class ErdesRenyiGraph:
    def __init__(self, n=1000, p=0.5):
        self.graph = nx.fast_gnp_random_graph(n, p)
        self.graph_length = len(self.graph)
        self.first_random_vertex = randint(0, self.graph_length / 2 - 1)
        self.second_random_vertex = randint(self.graph_length / 2, self.graph_length - 1)
    
    def info(self):
        return nx.info(self.graph)

    def vertex_degree(self):
        return self.graph.degree(self.first_random_vertex)

    def neighbors(self):
        return [vertex for vertex in self.graph.neighbors(self.first_random_vertex)]
    
    def triangles(self):
        return nx.triangles(self.graph, self.first_random_vertex)
    
    def shortest_path(self):
        return nx.shortest_path(self.graph, 
                                source=self.first_random_vertex, 
                                target=self.second_random_vertex)
    
    def graph_stats(self):
        print(nx.info(self.graph))
        print(f'First random vertex: {self.first_random_vertex}')
        print(f'Second random vertex: {self.second_random_vertex}')
        print(self.graph.degree(self.first_random_vertex))
        print([vertex for vertex in self.graph.neighbors(self.first_random_vertex)])
        print(nx.triangles(self.graph, self.first_random_vertex))
        print(nx.shortest_path(self.graph, source=self.first_random_vertex, target=self.second_random_vertex))


first_graph = ErdesRenyiGraph()
first_graph.graph_stats()
# print(nx.diameter(first_graph.graph))

second_graph = ErdesRenyiGraph(1000, 0.001)
second_graph.graph_stats()