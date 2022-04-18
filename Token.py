import re
import tkinter

#NUM = "[0-9]+"
#ID = "([a-z]|[A-Z])+"
#REGEX="REPEAT ([_a-zA-Z][_a-zA-Z0-9]* := (([_a-zA-Z]+[_a-zA-Z0-9]*)|[0-9]+);)+ UNTIL ([_a-zA-Z][_a-zA-Z0-9]* = ([_a-zA-Z0-9]+))"
rekt = input("please enter the Expression Required to be Checked ")
#v = re.search(
   # "REPEAT ([_a-zA-Z][_a-zA-Z0-9]* := (([_a-zA-Z]+[_a-zA-Z0-9]*)|[0-9]+);)+ UNTIL [_a-zA-Z][_a-zA-Z0-9]* = [_a-zA-Z0-9]+",
   # rekt)
#if v:
  #  print("YES ACCEPTED /n Reached Accepted State ")
#else:
  #  print("No match")
  #  x=re.split(" ",rekt)
   # print(x)
NUM = "[0-9]+"
ID = "([a-z]|[A-Z])+"
REGEX = f"(REPEAT\s*({ID}\s*:=\s*(({ID}|{NUM})\s*;\s*))+\s*UNTIL\s*({ID}\s*=\s*({ID}|{NUM})\s*))"
Exepresstion = re.fullmatch(REGEX, rekt)
if Exepresstion is None:
        print("WRONG")
else:
        print("TRUE")




