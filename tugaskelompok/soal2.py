import networkx as nx
import matplotlib.pyplot as plt

# Membuat graph
G = nx.Graph()

# Menambahkan edge dan cost
edges = [
    ("P", "Q", 4),
    ("P", "R", 3),
    ("Q", "R", 1),
    ("Q", "S", 4),
    ("R", "S", 5),
    ("S", "T", 3),
    ("S", "U", 6),
    ("T", "U", 4)
]

G.add_weighted_edges_from(edges)

# Posisi node
pos = {
    "P": (0, 1),
    "Q": (2, 2),
    "R": (2, 0),
    "S": (4, 1),
    "T": (6, 2),
    "U": (6, 0)
}

# Gambar node dan edge
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightgreen",
    node_size=2500,
    font_size=12,
    font_weight="bold"
)

# Ambil label cost
labels = nx.get_edge_attributes(G, 'weight')

# Tampilkan cost pada edge
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Graph Soal 2")
plt.axis("off")
plt.show()