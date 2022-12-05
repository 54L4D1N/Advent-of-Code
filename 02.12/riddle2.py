lines = []
opponent = ""
you = ""
opponentNum = 0
youNum = 0
points = 0


def makeStringToInt():
    global opponentNum
    opponentNum = 0
    if(opponent is "A"):
        opponentNum = 1
    elif(opponent is "B"):
        opponentNum = 2
    elif(opponent is "C"):
        opponentNum = 3

def winner():
    global points, you, youNum, opponentNum
    if(you is "Y"):
        youNum = opponentNum
        points = points + youNum + 3
    elif(you is "X"):
        if(opponentNum == 1):
            youNum = 3
        else:
            youNum = opponentNum - 1
        points = points + youNum
    elif(you is "Z"):
        if (opponentNum == 3):
            youNum = 1
        else:
            youNum = opponentNum + 1
        points = points + youNum + 6

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

for line in lines:
    line = line.rstrip("\n")
    opponent = line.split(" ")[0]
    you = line.split(" ")[1]
    makeStringToInt()
    winner()

print(points)
