lines = []
cals = []
cal = 0
calTop = 0

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

for line in lines:
    if(line is not "\n"):
        intLine = int(line.strip())
        cal = cal + intLine
    elif(line is "\n"):
        cals.append(cal)
        cal = 0

cals.sort(reverse=True)

calTop = cals[0]

print(calTop)
