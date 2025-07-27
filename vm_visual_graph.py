# vm_visual_graph.py

import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("User")
G.add_node("Web Dashboard")
G.add_node("VM1: Linux (AI)")
G.add_node("VM2: Windows")
G.add_node("Security Scan")
G.add_node("AI Model")

# Add connections
G.add_edges_from([
    ("User", "Web Dashboard"),
    ("Web Dashboard", "VM1: Linux (AI)"),
    ("Web Dashboard", "VM2: Windows"),
    ("VM1: Linux (AI)", "Security Scan"),
    ("VM1: Linux (AI)", "AI Model"),
    ("Security Scan", "VM2: Windows"),
    ("AI Model", "Web Dashboard")
])

# Position nodes
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="skyblue")
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

plt.title("🚀 VM Activity Visual: CyberSentinel")
plt.axis('off')
plt.tight_layout()
plt.show()
