input = '4-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

def is_contained(x, y):
    start, end = x
    start_y, end_y = y
    return start_y >= start and end_y <= end

def p1():
    contained_pairs = 0
    for line in read_input():
        first, second = line.split(',')
        f1, f2 = [int(x) for x in first.split('-')]
        s1, s2 = [int(x) for x in second.split('-')]
        if is_contained((f1, f2), (s1, s2)) or is_contained((s1, s2), (f1, f2)):
            contained_pairs += 1
    return contained_pairs

def dont_overlap(x, y):
    start, end = x
    start_y, end_y = y
    if start < start_y:
        return end < start_y
    return end_y < start

def is_overlapped(x, y):
    return not dont_overlap(x, y)

def p2():
    overlaps = 0
    for line in read_input():
        first, second = line.split(',')
        f1, f2 = [int(x) for x in first.split('-')]
        s1, s2 = [int(x) for x in second.split('-')]
        if is_overlapped((f1, f2), (s1, s2)):
            overlaps += 1
        
    return overlaps

print(p1())
print(p2())