import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from dfa import DFA

Accepted_token = {'REPEAT', 'NUM', 'UNTIL', 'ID', ';', ':=','=','<','>','>=','<='}
Token_transitions = {
    '1': {'REPEAT': '2'},
    '2': {'ID': '3'},
    '3': {':=': '4'},
    '4': {'ID': '5','NUM':'5'},
    '5': {';': '6'},
    '6': {'UNTIL': '7','ID':'3'},
    '7': {'ID': '8','NUM':'8'},
    '8': { '=': '9','<=': '9','>=': '9','<': '9','>': '9'},
    '9': {'ID': '10', 'NUM': '10'},
    '10': {},
    '11': {},



}

S = DFA(states=list(str(n) for n in range(1, 12)),
        input_symbols=Accepted_token,
        transitions=Token_transitions,
        initial_state='1',
        final_states={'10'})
print(Token_transitions)


node_pos = {
    '1': (100, 200),
    '2': (200, 200),
    '3': (300, 200),
    '4': (400, 200),
    '5': (500, 200),
    '6': (550, 260),
    '7': (700, 200),
    '8': (800, 200),
    '9': (900, 160),
    '10': (1000, 240),
    '11':(600,380),

}

G = Network(height='100%', width='100%', directed=True)
G.hrepulsion()
for state in S.states:
    G.add_node(int(state), shape="Circle", physics=False, x=node_pos[state][0], y=node_pos[state][1])

G.nodes[0]["color"] = 'orange'
G.nodes[0]["title"] = "Initial State"

G.nodes[9]["color"] = {"background": 'lime', "border": 'black'}
G.nodes[9]["borderWidth"] = 2
G.nodes[9]["borderWidthSelected"] = 2
G.nodes[9]["title"] = "Final State"

G.nodes[10]["label"] = 'S'
G.nodes[10]["color"] = 'grey'
G.nodes[10]["title"] = "Stuck State"
G.set_edge_smooth("curvedCW")
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

