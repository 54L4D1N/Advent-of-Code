crates = []
lines = []
counter = 1

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

def createStack():
    global crates, lines

    counter = 1
    for x in range(9):
        crateStack = [lines[0][counter], lines[1][counter], lines[2][counter], lines[3][counter], lines[4][counter], lines[5][counter], lines[6][counter], lines[7][counter]]
        crates.append(crateStack)
        counter = counter + 4

def removeCrates():
    for x in range(9):
        crates[x] = [x for x in crates[x] if x != ' ']

def moveCrates(number, fromX, toY):
    for x in range(number):
        crates[toY - 1].append(crates[fromX - 1][len(crates[fromX - 1]) - 1])
        crates[fromX - 1].pop(len(crates[fromX - 1]) - 1)

createStack()

for crateStack in crates:
    crateStack.reverse()

removeCrates()
print(crates)

counter = 0

for line in lines:
    counter = counter + 1
    if counter >= 11:
        line = line.rstrip("\n")
        allNumbers = [int(i) for i in line.split() if i.isdigit()]
        moveCrates(allNumbers[0], allNumbers[1], allNumbers[2])

print("\n")
print(crates)

topStack = ""
for crateStack in crates:
    topStack = topStack + crateStack[len(crateStack) - 1]

print("\n")
print(topStack)
