lines = []
group = []
sum = 0
counter = 0

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def makeStringToInt(string):
    global sum

    int = 0
    for char in characters:
        int = int + 1
        if (string is char):
            print(char)
            print(int)
            sum = sum + int

def sameCharacter():
    global char, group

    contains = False

    for char in characters:
#        if((char in group[0]) and (char in group[1]) and (char in group[2])):
 #           break
        for line in group:
            if(char in line):
                contains = True
            else:
                contains = False
                break
        if(contains):
            break

    return char

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

for line in lines:
    counter = counter + 1
    line = line.rstrip("\n")
    group.append(line)

    if(counter == 3):
        makeStringToInt(sameCharacter())
        counter = 0
        group = []

print(sum)
