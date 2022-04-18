import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from dfa import DFA
g=Network(height="500px",width="100%")
g.add_node(0)
g.add_node(1)
g.add_edge(0,1)
g.show("animated.html")
quit()
