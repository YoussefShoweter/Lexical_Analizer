import re
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


from dfa import DFA

def get_tokens_list(input_code):
    NUM = "[0-9]+"
    ID = "([a-z]|[A-Z])+"
    REGEX = f"(REPEAT\s*({ID}\s*:=\s*(({ID}|{NUM})\s*;\s*))+\s*UNTIL\s*({ID}\s*=\s*({ID}|{NUM})\s*))"
    # rekt = re.fullmatch(REGEX, input_code)
    tokens_list = []
    tokens = re.findall('REPEAT|[0-9]+|UNTIL|[_a-zA-Z][_a-zA-Z0-9]*|:=|;|=', input_code)
    for token in tokens:
        if token == "REPEAT":
            tokens_list.append({"token": token, "type": "REPEAT"})
        elif token == "UNTIL":
            tokens_list.append({"token": token, "type": "UNTIL"})
        elif token == ":=":
            tokens_list.append({"token": token, "type": ":="})
        elif token == "=":
            tokens_list.append({"token": token, "type": "="})
        elif token == ";":
            tokens_list.append({"token": token, "type": ";"})
        elif re.search("[0-9]+", token) is not None:
            tokens_list.append({"token": token, "type": "NUM"})
        elif re.search("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
            tokens_list.append({"token": token, "type": "ID"})
        else:
            tokens_list.append({"token": token, "type": "UNKNOWN"})
            raise Exception("Invalid token returned from tokenization")
            print("error")


    return tokens_list

def check(input_code):
    NUM = "[0-9]+"
    ID = "[_a-zA-Z]\w*"
    REGEX = f"(REPEAT\s*({ID}\s*:=\s*(({ID}|{NUM})\s*;\s*))+\s*UNTIL\s*({ID}\s*=\s*({ID}|{NUM})\s*))"
    rekt = re.fullmatch(REGEX, input_code)
    if rekt is None:
        return "Wrong Syntax of Repeat Untill Statement"
    else:
        return "Correct Syntax Match"