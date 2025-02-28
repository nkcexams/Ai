import networkx as nx

# Load graph
try:
    G = nx.read_graphml(r"newyork.graphml")
except Exception as e:print(f"Error loading graph: {e}") , exit()

# Convert MultiGraph to simple Graph if necessary
if G.is_multigraph(): G = nx.Graph(G)

print(f"Density: {nx.density(G):.4f}")
print("\nDegree (first 5 nodes):", dict(list(G.degree())[:5]))

# Reciprocity only for directed graphs
print(f"\nReciprocity: {nx.reciprocity(G):.4f}" if G.is_directed() else "\nReciprocity not applicable.")

# Use transitivity if possible, otherwise use average clustering
print(f"\nTransitivity: {nx.transitivity(G):.4f}" if not G.is_multigraph() else 
      f"\nUsing average clustering: {nx.average_clustering(G):.4f}")

print("\nCentrality (first 5 nodes):", dict(list(nx.degree_centrality(G).items())[:5]))
print("\nClustering (first 5 nodes):", dict(list(nx.clustering(G).items())[:5]))



