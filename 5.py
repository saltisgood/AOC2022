input = '5-input.txt'

NUM_STACKS = 9

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

def parse_header(lines: list[str]):
    stacks = []
    for _ in range(NUM_STACKS):
        stacks.append([])
    
    for line in lines:
        for i in range(NUM_STACKS):
            try:
                c = line[(4 * i) + 1]
            except IndexError:
                continue
            if c != ' ':
                stacks[i].insert(0, c)
    return stacks

def parse_move(move):
    _, qty, _, f, _, t = move.split(' ')
    return int(qty), int(f) - 1, int(t) - 1

def make_move(stacks, move):
    qty, f, t = parse_move(move)
    for _ in range(qty):
        stacks[t].append(stacks[f].pop())

def make_move_v2(stacks : list[list], move):
    qty, f, t = parse_move(move)
    stacks[t].extend(stacks[f][-qty:])
    stacks[f] = stacks[f][:-qty]

def p1():
    stacks = None
    header_lines = []
    for line in read_input():
        if stacks is None:
            if line:
                header_lines.append(line)
            else:
                stacks = parse_header(header_lines)
        else:
            make_move(stacks, line)

    return ''.join(x[-1] for x in stacks)

def p2():
    stacks = None
    header_lines = []
    for line in read_input():
        if stacks is None:
            if line:
                header_lines.append(line)
            else:
                stacks = parse_header(header_lines)
        else:
            make_move_v2(stacks, line)

    return ''.join(x[-1] for x in stacks)

print(p1())
print(p2())