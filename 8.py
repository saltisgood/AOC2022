from dataclasses import dataclass
from typing import List

input = '8-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

TOP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

@dataclass
class Tree:
    height: int
    visible: list[bool]
    scenic_visible: list[int]

    def __init__(self, height):
        self.height = height
        self.visible = [False, False, False, False]
        self.scenic_visible = [0, 0, 0, 0]

    def set_visible(self, d):
        self.visible[d] = True
    
    @property
    def is_visible(self):
        return any(self.visible)
    
    def set_scenic_visible(self, d, v):
        self.scenic_visible[d] = v
    
    def get_scenic_visible(self, d):
        return self.scenic_visible[d]
    
    @property
    def scenic_score(self):
        prod = 1
        for v in self.scenic_visible:
            prod *= v
        return prod

def calc_visible(trees: list[Tree], direction):
    prev_height = -1
    for tree in trees:
        if tree.height > prev_height:
            prev_height = tree.height
            tree.set_visible(direction)
        else:
            continue

def calc_scenic_impl(root: Tree, trees: list[Tree], direction):
    count = 0
    for tree in reversed(trees):
        count += 1
        if tree.height >= root.height:
            break
    root.set_scenic_visible(direction, count)

def calc_scenic(trees: list[Tree], direction):
    for i in range(len(trees)):
        calc_scenic_impl(trees[i], trees[:i], direction)

@dataclass
class Grid:
    rows: List[List[Tree]]

    def __init__(self):
        self.rows = []

    def add_row(self, r):
        new_row = []
        for h in r:
            new_row.append(Tree(int(h)))
        self.rows.append(new_row)
    
    def calc_top(self):
        width = len(self.rows[0])
        for x in range(width):
            calc_visible((r[x] for r in self.rows), TOP)

    def calc_right(self):
        for row in self.rows:
            calc_visible(reversed(row), RIGHT)
    
    def calc_down(self):
        width = len(self.rows[0])
        for x in range(width):
            calc_visible((r[x] for r in reversed(self.rows)), DOWN)
    
    def calc_left(self):
        for row in self.rows:
            calc_visible(row, LEFT)
    
    def calc(self):
        self.calc_top()
        self.calc_right()
        self.calc_down()
        self.calc_left()
    
    @property
    def visible_trees(self):
        visible = 0
        for row in self.rows:
            for t in row:
                if t.is_visible:
                    visible += 1
        return visible
    
    def print_visible_grid(self):
        for row in self.rows:
            print(''.join(('T' if t.is_visible else 'F') for t in row))
    
    def print_scenic_grid(self):
        for row in self.rows:
            print(''.join(str(x) for x in (t.scenic_score for t in row)))
    
    def calc_scenic(self):
        width = len(self.rows[0])
        for x in range(width):
            calc_scenic([r[x] for r in self.rows], TOP)
        for row in self.rows:
            calc_scenic(list(reversed(row)), RIGHT)
        for x in range(width):
            calc_scenic([r[x] for r in reversed(self.rows)], DOWN)
        for row in self.rows:
            calc_scenic(row, LEFT)
    
    @property
    def max_scenic(self):
        return max(max(t.scenic_score for t in row) for row in self.rows)

def parse_input(input):
    g = Grid()

    for row in input:
        g.add_row(row)
    
    return g

def p1():
    g = parse_input(read_input())
    g.calc()
    return g.visible_trees

def p2():
    g = parse_input(read_input())
    g.calc_scenic()
    return g.max_scenic

def do_sample_p1():
    input = """30373
25512
65332
33549
35390""".splitlines()
    g = parse_input(input)
    breakpoint()
    g.calc()
    print(g.visible_trees)
    g.print_visible_grid()

def do_sample_p2():
    input = """30373
25512
65332
33549
35390""".splitlines()
    g = parse_input(input)
    breakpoint()
    g.calc_scenic()
    print(g.max_scenic)
    g.print_scenic_grid()

#do_sample_p1()
do_sample_p2()
print(p1())
print(p2())