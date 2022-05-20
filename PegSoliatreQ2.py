import re
from datetime import datetime
start_time = datetime.now()
# do your work here

def CreateSolitare(n):
    return [1]*n
FailedMoves =[]

def solveSolitare(Solitare):
    global FailedMoves
    if isValidSoln(Solitare):

        print("Next Solved Position Below")
        print(Solitare)

        return True
    elif checkUnsolvable(Solitare):
        return False

    AllPossibleMoves = []
    for i in range(len(Solitare)):
        if i < -2+len(Solitare): #to make sure there is even a space to move right
            if Solitare[i] and Solitare[i + 1] and not Solitare[i + 2]:
                AllPossibleMoves.append((i, 'right'))
        if i > 1:  #to make sure there is even a space to move left
            if Solitare[i] and Solitare[i - 1] and not Solitare[i - 2]:
                AllPossibleMoves.append((i, 'left'))

    
    for Step in AllPossibleMoves:
        NewSolitaire = CreateNewMove(Solitare, Step)
        if solveSolitare(NewSolitaire):
            print(Solitare)
            return True
        else:
            FailedMoves.append(''.join([str(n) for n in Solitare]))

        continue

    return False

def CreateNewMove(Solitare, Step):
    index, direction = Step
    Position = [element for element in Solitare]
    if direction == 'right':
        Position[index] = 0
        Position[index+1] = 0
        Position[index+2] = 1
    elif direction == 'left':
        Position[index] = 0
        Position[index-1] = 0
        Position[index-2] = 1
    return Position

def isValidSoln(Solitare):
    if sum(Solitare) == 1:
        return True
    return False

def checkUnsolvable(Solitare):
    global FailedMoves
    if''.join([str(n)for n in Solitare]) in FailedMoves:
        return True
    FailedExp1 = '00100'
    FailedEXp2 =   '1000+1'
    string = ''.join([str(element) for element in Solitare])
    if re.search(FailedExp1, string) or re.search(FailedEXp2, string):
        return True
    return False

def countSolutions(Solitare):

    SuccesfulPositions = []
    for i in range(len(Solitare)):
        temp = [element for element in Solitare]
        temp[i] = 0
        if solveSolitare(temp):
            SuccesfulPositions.append(i+1)


    return SuccesfulPositions




print("Please Enter the Size of the Required Solitare")
print()
print("Note: if more than 1 index found succefuly to solve the Solutio  path will be Printed in the Assending order of the Indicies")
n = int(input())
print(countSolutions(CreateSolitare(n)))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))