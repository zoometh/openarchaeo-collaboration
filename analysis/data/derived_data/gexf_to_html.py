import os
import networkx as nx
from pyvis.network import Network

print(os.getcwd())

# Load GEXF file
g = nx.read_gexf('C:/Rprojects/openarchaeo-collaboration/analysis/data/derived_data/oarch_repo_repo.gexf')

# Initialize PyVis network object
nt = Network('500px', '500px')

# Take the NetworkX graph and translate it to a PyVis graph format
nt.from_nx(g)

# Save to HTML file
nt.show('graph.html')
