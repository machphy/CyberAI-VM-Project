import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with layers (for manual layout)
layers = {
    "User": 5,
    "Web Dashboard": 4,
    "VM1: Linux (AI)": 3,
    "VM2: Windows": 3,
    "AI Model": 2,
    "Security Scan": 2,
    "Log/Alert Output": 1
}

# Add nodes
for node in layers:
    G.add_node(node, layer=layers[node])

# Add directed edges (connections)
edges = [
    ("User", "Web Dashboard"),
    ("Web Dashboard", "VM1: Linux (AI)"),
    ("Web Dashboard", "VM2: Windows"),
    ("VM1: Linux (AI)", "AI Model"),
    ("VM1: Linux (AI)", "Security Scan"),
    ("VM2: Windows", "Security Scan"),
    ("AI Model", "Log/Alert Output"),
    ("Security Scan", "Log/Alert Output")
]

G.add_edges_from(edges)

# Custom position based on layers
pos = {}
x_gap = 2
y_gap = 1.5
layer_nodes = {}

# Group nodes by layer
for node, layer in layers.items():
    layer_nodes.setdefault(layer, []).append(node)

# Position nodes layer by layer
for layer, nodes in layer_nodes.items():
    for i, node in enumerate(nodes):
        pos[node] = (i * x_gap, -layer * y_gap)

# Draw the graph
plt.figure(figsize=(12, 7))
nx.draw_networkx_nodes(G, pos, node_color="lightgreen", node_size=2000)
nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

plt.title("🧠 CyberAI VM Architecture - Layered Flow", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
