from random import randint
import matplotlib.pyplot as mpl
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
        print(type(self.graph.degree(self.first_random_vertex)))
        return self.graph.degree(self.first_random_vertex)

    def neighbors(self):
        return [vertex for vertex in self.graph.neighbors(self.first_random_vertex)]
    
    def triangles(self):
        return nx.triangles(self.graph, self.first_random_vertex)
    
    def shortest_path(self):
        try:
            return nx.shortest_path(self.graph, 
                                    source=self.first_random_vertex, 
                                    target=self.second_random_vertex)
        except nx.NetworkXNoPath:
            return f'Кратчайший путь между вершинами {self.first_random_vertex} '\
                   f'и {self.second_random_vertex} не существует!'

    def shortest_path_length(self):
        try:
            return nx.shortest_path_length(self.graph, 
                                           source=self.first_random_vertex,
                                           target=self.second_random_vertex)
        except nx.NetworkXNoPath:
            return f'Кратчайшее расстояние между вершинами {self.first_random_vertex} '\
                   f'и {self.second_random_vertex} не существует!'

    def distribution(self):
        return [vertex[1] for vertex in nx.degree(self.graph)]

    def graph_stats(self):
        print(nx.info(self.graph))
        print(f'First random vertex: {self.first_random_vertex}')
        print(f'Second random vertex: {self.second_random_vertex}')
        print(f'Graph degree: {self.vertex_degree()}')
        print(f'Neighbours: {[vertex for vertex in self.graph.neighbors(self.first_random_vertex)]}')
        print(f'Triangles: {self.triangles()}')
        print(f'Shortest path length: {self.shortest_path_length()}')
        print(f'Shortest path: {self.shortest_path()}')
        print(f'Graph distribution: {self.distribution()}')

first_graph = ErdesRenyiGraph()
# first_graph.graph_stats()

def bfs(g, v):
    pass

def diameterTree(g):
    v, u, w = 0
    d = bfs(g, v)
    n = g.graph_length
    for i in range(n):
        if d[i] > d[u]:
            u = i
    bfs(g, u)
    for i in range(n):
        if d[i] > d[w]:
            w = i
    return d[w]

mpl.hist(first_graph.distribution())
mpl.show()

second_graph = ErdesRenyiGraph(1000, 0.001)
# second_graph.graph_stats()
mpl.hist(second_graph.distribution())
mpl.show()
