import sys
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        G = nx.Graph()

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

                    # Agregar la arista al grafo
                    G.add_edge(u, v, weight=self.graph[u][v])
                    self.plot_graph(G, parent, u, v)

    def plot_graph(self, G, parent, u, v):
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        plt.clf()
        plt.title("Árbol de Expansión Mínima (Prim)")

        edge_colors = ['g' if (u, v) == (parent[v], v) else 'r' for u, v in G.edges()]
        node_colors = ['g' if i == v else 'b' for i in G.nodes()]

        nx.draw_networkx_nodes(G, pos, node_color=node_colors)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=edge_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.show()
        plt.pause(1)

g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

plt.ion()
g.prim_mst()
plt.ioff()
