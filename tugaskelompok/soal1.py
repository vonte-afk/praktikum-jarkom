import networkx as nx
import matplotlib.pyplot as plt

# Membuat graph
G = nx.Graph()

# Menambahkan edge dan cost
edges = [
    ("A", "B", 2),
    ("A", "C", 4),
    ("B", "C", 1),
    ("B", "D", 6),
    ("C", "D", 1),
    ("C", "E", 7),
    ("D", "E", 3)
]

G.add_weighted_edges_from(edges)

# Posisi node
pos = {
    "A": (0, 1),
    "B": (2, 1),
    "C": (1, 0),
    "D": (3, 0),
    "E": (4, -1)
}

# Gambar node dan edge
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2500,
    font_size=12,
    font_weight="bold"
)

# Ambil label cost
labels = nx.get_edge_attributes(G, 'weight')

# Tampilkan cost pada edge
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Graph Soal 1")
plt.axis("off")
plt.show()