lines = []
opponent = ""
you = ""
opponentNum = 0
youNum = 0
points = 0


def makeStringToInt(string):
    global int
    int = 0
    if(string is "A" or string is "X"):
        int = 1
    elif(string is "B" or string is"Y"):
        int = 2
    elif(string is "C" or string is "Z"):
        int = 3

    return int

def winner():
    global points
    if(youNum == opponentNum):
        points = points + youNum + 3
    elif((youNum == 1 and opponentNum == 3) or (youNum == 2 and opponentNum == 1) or (youNum == 3 and opponentNum == 2)):
        points = points + youNum + 6
    elif((youNum == 1 and opponentNum == 2) or (youNum == 2 and opponentNum == 3) or (youNum == 3 and opponentNum == 1)):
        points = points + youNum

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

for line in lines:
    line = line.rstrip("\n")
    opponent = line.split(" ")[0]
    you = line.split(" ")[1]
    opponentNum = makeStringToInt(opponent)
    youNum = makeStringToInt(you)
    winner()

print(points)
