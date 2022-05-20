
test1=[2,1,2,2,3,4,2,3,1,1,2,2,2,4,4,4,2,2,3,3,1,1]
test1r=[2,1,2,2,3,4,2,3,1,1,2,2,2,4,4,4,2,2,3,3,1,1]

test2=[2,3,3,4,1,1,2,2,2,3,3,4,3,3,2,2,4,4,1,2,1,1]
youssef=[1,2,1,1,4,2,1,4,2,1,3,3,4,2,1,4,2,1,4,3]

def solve(youssef):
    for i in range( 0,len(youssef) - 1, 1):
        for j in range( 0,len(youssef) - 1, 1):
            if youssef[j+1]==3 and youssef[j]==1:
                temp=youssef[j]
                youssef[j]=youssef[j+1]
                youssef[j + 1]=temp
            if youssef[j + 1] == 3 and youssef[j] == 2:
                temp = youssef[j]
                youssef[j] = youssef[j + 1]
                youssef[j + 1] = temp
            if youssef[j + 1] == 3 and youssef[j] == 4:
                temp = youssef[j]
                youssef[j] = youssef[j + 1]
                youssef[j + 1] = temp
            if youssef[j + 1] == 3 and youssef[j] == 1:
                temp = youssef[j]
                youssef[j] = youssef[j + 1]
                youssef[j + 1] = temp
            if youssef[j+1]==2 and youssef[j]==4:
                temp=youssef[j]
                youssef[j]=youssef[j+1]
                youssef[j + 1]=temp
            if youssef[j+1]==1 and youssef[j]==2:
                temp=youssef[j]
                youssef[j]=youssef[j+1]
                youssef[j + 1]=temp
            if youssef[j+1]==1 and youssef[j]==4:
                temp=youssef[j]
                youssef[j]=youssef[j+1]
                youssef[j + 1]=temp
# solve(youssef)
# print(youssef)
#
# solve(test1)
# print(test1)
#
# solve(test2)
# print(test2)

def getValue(n):
    if n == 3:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 3

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if getValue(arr[j]) > getValue(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


sort(test1)
print(test1)

solve(test1r)
print(test1r)
