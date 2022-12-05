lines = []
sum = 0

with open('input.txt') as file:
    for line in file.readlines():
        lines.append(line)

def test(part1, part2):
    global sum

    if int(part1[0]) <= int(part2[0]) and int(part1[1]) >= int(part2[1]):
        sum = sum + 1
    elif int(part2[0]) <= int(part1[0]) and int(part2[1]) >= int(part1[1]):
        sum = sum + 1

for line in lines:
    line = line.rstrip("\n")
    part1 = line.split(",")[0].split("-")
    part2 = line.split(",")[1].split("-")
    test(part1, part2)

print(sum)
