import networkx as nx
import matplotlib.pyplot as plt

def kruskal(graph):
    graph = sorted(graph, key=lambda x: x[2])  # Ordena las aristas por peso en orden ascendente
    tree = []
    disjoint_sets = {}

    def find_set(node):
        if node != disjoint_sets[node]:
            disjoint_sets[node] = find_set(disjoint_sets[node])
        return disjoint_sets[node]

    def union(u, v):
        root_u = find_set(u)
        root_v = find_set(v)
        if root_u != root_v:
            disjoint_sets[root_u] = root_v
            return True
        return False

    for u, v, weight in graph:
        if u not in disjoint_sets:
            disjoint_sets[u] = u
        if v not in disjoint_sets:
            disjoint_sets[v] = v

        if union(u, v):
            tree.append((u, v, weight))

    return tree

# Ejemplo de uso
graph = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 3), (2, 3, 5)]
minimum_spanning_tree = kruskal(graph)

# Visualización del grafo original y el árbol de expansión mínima
G = nx.Graph()
G.add_weighted_edges_from(graph)
T = nx.Graph()
T.add_weighted_edges_from(minimum_spanning_tree)

pos = nx.spring_layout(G)

plt.figure(figsize=(12, 6))
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_size=500)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo Original')

plt.subplot(122)
nx.draw(T, pos, with_labels=True, node_size=500)
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
plt.title('Árbol de Expansión Mínima (Kruskal)')

plt.show()
