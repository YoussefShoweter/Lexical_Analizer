import re
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


from dfa import DFA

def Obtain_Tokens_from_text0(input_code):

    tokens_list = []
    tokens = re.findall('REPEAT|[0-9]+|UNTIL|[_a-zA-Z][_a-zA-Z0-9]*|:=|;|=|>|<|<=|=>', input_code)
    for token in tokens:
        if token == "REPEAT":
            tokens_list.append({"token": token, "type": "REPEAT"})
        elif token == "UNTIL":
            tokens_list.append({"token": token, "type": "UNTIL"})
        elif token == ":=":
            tokens_list.append({"token": token, "type": ":="})
        elif token == "=>":
            tokens_list.append({"token": token, "type": ">="})
        elif token == "<=":
            tokens_list.append({"token": token, "type": "<="})
        elif token == "<":
            tokens_list.append({"token": token, "type": "<"})
        elif token == "=":
            tokens_list.append({"token": token, "type": "="})
        elif token == ">":
            tokens_list.append({"token": token, "type": ">"})
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

def Obtain_Tokens_from_text1(input_code):
    tokens_list = []
    tokens = re.findall('repeat|[0-9]+|until|[_a-zA-Z][_a-zA-Z0-9]*|:=|;|=|>|<|<=|=>', input_code)
    for token in tokens:
        if token == "repeat":
            tokens_list.append({"type": "repeat"})
        elif token == "until":
            tokens_list.append({ "type": "until"})
        elif token == ":=":
            tokens_list.append({"type": ":="})
        elif token == ";":
            tokens_list.append({"type": ";"})
        elif re.search("[0-9]+", token) is not None:
            tokens_list.append({ "type": "NUM"})
        elif re.search("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
            tokens_list.append({"type": "ID"})
        else:
            tokens_list.append({"token": token, "type": "UNKNOWN"})
            raise Exception("Invalid token returned from tokenization")
            print("error")



    tokens_list.append({"type":"$"})


    return tokens_list


def check(input_code):
    NUM = "[0-9]+"
    ID = "[_a-zA-Z]\w*"
    REGEX = f"(REPEAT\s*({ID}\s*:=\s*(({ID}|{NUM})\s*;\s*))+\s*UNTIL\s*(({ID}|{NUM})\s*(=|>|<|=>|<=)\s*({ID}|{NUM})\s*))"

    REGEX2 = f"(REPEAT\s*({ID}\s*:=\s*(({ID}|{NUM})\s*;\s*))+\s*UNTIL\s*({ID}\s*(=|>|<|=>|<=)\s*{NUM}\s*|{NUM}\s*(=|>|<|=>|<=)\s*{ID}\s*))"

    rekt = re.fullmatch(REGEX2, input_code)
    if rekt is None:
        return "Unaccepted ...Wrong Syntax "
    else:
        return "ACCEPTED  ...Correct Syntax"