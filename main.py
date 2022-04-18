print("Team Gandalf")

switches=[1,1,1,1,1,1,1,1,1,1]
switches[len(switches)-2]=0
switches[len(switches)-1]=0
x=len(switches)

if x%2==0:
    print("even")
else:
    print("odd")

print(switches)





