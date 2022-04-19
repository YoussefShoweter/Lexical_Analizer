import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#STATIC DFA --UNUSED--
G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
edges=([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(6,3),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),])
G.add_edges_from(edges)
labels = {(1,2):'REPEAT', (2,3):'ID',(3,4):':=', (4,5):'ID|NUM',(5,6):';', (6,7):'UNTILL',
          (7,8):'ID', (8,9):':=',(9,10):'ID|NUM', (6,3):'ID',
          (1, 11): '~REPEAT', (2, 11): '~ID', (3, 11): '~(:=)', (4, 11): '~(ID|NUM)', (5, 11): '~;', (6, 11): '~UNTILL',
          (7, 11): '~ID', (8, 11): '~(:=)', (9, 11): '~(ID|NUM)'
          }

pos=nx.circular_layout(G)
nx.draw(G, pos,with_labels=True,node_size=700,node_color='red')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=9)

G.edges(data=True)

plt.show()

