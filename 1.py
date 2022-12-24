input = '1-input.txt'

# P1
def p1():
    max_calories = 0
    current_calories = 0
    for line in open(input, 'r').readlines():
        line = line.strip()
        if line:
            current_calories += int(line)
        else:
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0

    print(max_calories)

def p2():
    elves = []
    current_calories = 0
    for line in open(input, 'r').readlines():
        line = line.strip()
        if line:
            current_calories += int(line)
        else:
            elves.append(current_calories)
            current_calories = 0
    elves.sort(reverse=True)
    print(sum(elves[:3]))

p1()
p2()