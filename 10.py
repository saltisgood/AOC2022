from dataclasses import dataclass

input = '10-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

def sample_input():
    return """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

class Cpu:
    def __init__(self, handler):
        self.cycle = 1
        self.handler = handler
        self.register = 1
    
    def give_instruction(self, instruction: str):
        if instruction == 'noop':
            self.noop()
        elif instruction.startswith('addx'):
            self.addx(int(instruction[5:]))
    
    def noop(self):
        self.callout()
        self.cycle += 1

    def addx(self, val: int):
        self.noop()
        self.noop()
        self.register += val

    def callout(self):
        self.handler(self.cycle, self.register)

def print_state(cycle, register):
    print(f'During cycle {cycle}: {register}')

@dataclass
class Tracker:
    sum: int = 0

    def __call__(self, cycle, register):
        if cycle in [20, 60, 100, 140, 180, 220]:
            self.sum += cycle * register

def p1():
    t = Tracker()
    c = Cpu(t)
    for line in read_input():
        c.give_instruction(line)
    return t.sum

class Crt:
    def __init__(self):
        self.screen_lines = [[]]

    def __call__(self, cycle, register):
        crt_pos = (cycle - 1) % 40
        if abs(crt_pos - register) <= 1:
            self.screen_lines[-1].append('#')
        else:
            self.screen_lines[-1].append('.')
        if cycle % 40 == 0:
            self.screen_lines.append([])
        self.print()

    def print(self):
        for line in self.screen_lines:
            print(''.join(line))

def p2():
    crt = Crt()
    cpu = Cpu(crt)
    for line in read_input():
        cpu.give_instruction(line)
    crt.print()

print(p1())
print(p2())