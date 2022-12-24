input = '3-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

def parse_line(line):
    n = int(len(line) / 2)
    return line[:n], line[n:]

def find_repeat(x):
    s = set(x[0])
    for i in range(1, len(x)):
        s &= set(x[i])
    return s.pop()

def priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1

def p1():
    priority_sum = 0
    for line in read_input():
        compart1, compart2 = parse_line(line)
        repeat = find_repeat([compart1, compart2])
        priority_sum += priority(repeat)
    return priority_sum

def p2():
    priority_sum = 0
    group = []
    for line in read_input():
        group.append(line)
        if len(group) == 3:
            repeat = find_repeat(group)
            priority_sum += priority(repeat)
            group.clear()
    return priority_sum

print(p1())
print(p2())