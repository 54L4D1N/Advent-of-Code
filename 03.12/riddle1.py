lines = []
sum = 0
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

    sum = sum + int

def sameCharacter(part1, part2):
    global char

    for char in part1:
        if char in part2:
            char
            break

    return char

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

for line in lines:
    line = line.rstrip("\n")
    part1 = slice(0, len(line)//2)
    part2 = slice(len(line)//2, len(line))
    makeStringToInt(sameCharacter(line[part1], line[part2]))

print(sum)
