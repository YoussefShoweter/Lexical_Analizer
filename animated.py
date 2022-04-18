import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from dfa import DFA

tiny_symbols = {'REPEAT', 'NUM', 'UNTIL', 'ID', ';', ':='}
tiny_transitions = {
    '1': {'REPEAT': '2'},
    '2': {'ID': '3'},
    '3': {':=': '4'},
    '4': {'ID': '5','NUM':'5'},
    '5': {';': '6'},
    '6': {'UNTIL': '7'},
    '7': {'ID': '8'},
    '8': { ':=': '9'},
    '9': {'ID': '10', 'NUM': '10'},
    '10': {'NUM': '11'},
    '11': {},
    '12': {},


}

S = DFA(states=list(str(n) for n in range(1, 13)),
        input_symbols=tiny_symbols,
        transitions=tiny_transitions,
        initial_state='1',
        final_states={'11'})
print(tiny_transitions)


node_pos = {
    '1': (100, 200),
    '2': (200, 200),
    '3': (300, 200),
    '4': (400, 200),
    '5': (500, 200),
    '6': (600, 200),
    '7': (700, 200),
    '8': (700, 100),
    '9': (800, 40),
    '10': (400, 0),
    '11': (900, 200),
    '12':(600,100),

}

G = Network(height='100%', width='100%', directed=True)
G.hrepulsion()
for state in S.states:
    G.add_node(int(state), shape="ellipse", physics=False, x=node_pos[state][0], y=node_pos[state][1])

G.nodes[0]["color"] = 'Blue'
G.nodes[0]["title"] = "Initial State"

G.nodes[11]["color"] = {"background": 'lime', "border": 'orange'}
G.nodes[11]["borderWidth"] = 5
G.nodes[11]["borderWidthSelected"] = 5
G.nodes[11]["title"] = "Goal State"

G.nodes[12]["label"] = 'D'
G.nodes[12]["color"] = 'DarkGray'
G.nodes[12]["title"] = "Dead State"

for k in S.states:
    for kk in S.transitions[k]:
        G.add_edge(int(k), int(S.transitions[k][kk]), label=kk)

G.set_options("""
var options = {
                  "edges": {
                    "smooth": {
                        "enabled" : true
                    }
                  },
                  "interaction": {
                    "hover": true,
                    "keyboard": {
                      "enabled": true
                    },
                    "multiselect": true,
                    "navigationButtons": true
                  }
                }
""")
G.save_graph("animated.html")
