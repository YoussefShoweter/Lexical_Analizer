import re
import tkinter

NUM = "[0-9]+"
ID = "([a-z]|[A-Z])+"

rekt = input("please enter the Expression Required to be Checked")
v = re.search(
    "REPEAT ([_a-zA-Z][_a-zA-Z0-9]* := (([_a-zA-Z]+[_a-zA-Z0-9]*)|[0-9]+);)+ UNTIL ([_a-zA-Z][_a-zA-Z0-9]* = ([_a-zA-Z0-9]+))",
    rekt)
if v:
    print("YES ACCEPTED")
else:
    print("No match")

