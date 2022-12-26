input = '6-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

def has_no_repeat(packet):
    return len(set(packet)) == len(packet)

def find(line, size=4):
    for i in range(len(line) - size):
        frame = line[i:i+size]
        if has_no_repeat(frame):
            return i + size

def p1():
    return find(next(read_input()))

def p2():
    return find(next(read_input()), size=14)

#print(find('bvwbjplbgvbhsrlpgdmjqwftvncz'))
#print(find('nppdvjthqldpwncqszvftbrmjlhg'))
#print(find('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))
print(p1())
print(p2())