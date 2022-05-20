#SecuritySoln Function solves the Bridge with less 2 indexes per call untill it reaches one of the base cases
#then if its odd or even the algo will work a bit differently

def CreateTower(n):
    return [1]*n
def Switch(SecurityBridge, i):
    if SecurityBridge[i] == 0:
        SecurityBridge[i] = 1
        print(SecurityBridge)
    else:
        SecurityBridge[i] = 0
        print(SecurityBridge)

def Allgood(SecurityBridge):
    for element in SecurityBridge:
        if element != 1:
            return False
    return True

def SecuritySoln(SecurityBridge, Steps, n):
    length = len(SecurityBridge)
    i = length - n

    if n > 2:
        SecuritySoln(SecurityBridge, Steps, n - 2)

    elif n == 2:
        Switch(SecurityBridge, i)
        Steps.append(i)
        Switch(SecurityBridge, i + 1)
        Steps.append(i + 1)
        return
    elif n == 1:
        Switch(SecurityBridge, i)
        Steps.append(i)
        return

    Switch(SecurityBridge, i) #if the board reached here then the index can be switched and the fellow right is 1 and evry other right is 0
    Steps.append(i)

    for j in range(len(Steps) - 1, -1, -1):
        if Steps[j] < i+1:
            continue
        if Allgood(SecurityBridge[i + 2:]):
            break
        Switch(SecurityBridge, Steps[j])
        Steps.append(Steps[j])

    SecuritySoln(SecurityBridge, Steps, n - 1)


n = int(input())
Bridge = CreateTower(n)
print(Bridge)

NumOfMoves = []
SecuritySoln(Bridge, NumOfMoves, n)
print(len(NumOfMoves))
