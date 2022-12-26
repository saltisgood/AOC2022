from dataclasses import dataclass

GRID_WIDTH = 1000
GRID_HEIGHT = 1000

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 2

input = '9-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

def sample_input():
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

@dataclass
class Cell:
    tail_visited: bool = False

class Grid:
    def __init__(self):
        self.rows = list[list[Cell]]()
        for y in range(GRID_HEIGHT):
            row = []
            for x in range(GRID_WIDTH):
                row.append(Cell())
            self.rows.append(row)
        start = (int(GRID_WIDTH / 2), int(GRID_HEIGHT / 2))
        self.tail_pos = start
        self.head_pos = start
        self.start_pos = start
        self.cell(start).tail_visited = True
    
    def cell(self, pos):
        return self.rows[pos[1]][pos[0]]
    
    def move(self, dir, num: int):
        for _ in range(num):
            if dir == 'R':
                self.head_pos = (self.head_pos[0] + 1, self.head_pos[1])
            elif dir == 'L':
                self.head_pos = (self.head_pos[0] - 1, self.head_pos[1])
            elif dir == 'U':
                self.head_pos = (self.head_pos[0], self.head_pos[1] - 1)
            else:
                self.head_pos = (self.head_pos[0], self.head_pos[1] + 1)
            self.move_tail()
            #self.dump()
    
    def move_pos(self, pos, x_diff, y_diff):
        new_x, new_y = pos
        new_x += x_diff
        new_y += y_diff
        new_x = new_x % GRID_WIDTH
        new_y = new_y % GRID_HEIGHT
        return (new_x, new_y)
    
    def is_touching(self, pos1, pos2):
        diff_x = abs(pos1[0] - pos2[0])
        diff_y = abs(pos1[1] - pos2[1])
        return diff_x < 2 and diff_y < 2

    def move_tail(self):
        if self.is_touching(self.head_pos, self.tail_pos):
            return
        diff_x = self.head_pos[0] - self.tail_pos[0]
        diff_y = self.head_pos[1] - self.tail_pos[1]
        if diff_x == 2:
            self.tail_pos = self.move_pos(self.tail_pos, 1, diff_y)
        elif diff_x == -2:
            self.tail_pos = self.move_pos(self.tail_pos, -1, diff_y)
        elif diff_y == 2:
            self.tail_pos = self.move_pos(self.tail_pos, diff_x, 1)
        elif diff_y == -2:
            self.tail_pos = self.move_pos(self.tail_pos, diff_x, -1)
        # Diags
        elif self.head_pos[0] > self.tail_pos[0] and self.head_pos[1] > self.tail_pos[1]:
            self.tail_pos = self.move_pos(self.tail_pos, 1, 1)
        elif self.head_pos[0] > self.tail_pos[0] and self.head_pos[1] < self.tail_pos[1]:
            self.tail_pos = self.move_pos(self.tail_pos, 1, -1)
        elif self.head_pos[0] < self.tail_pos[0] and self.head_pos[1] > self.tail_pos[1]:
            self.tail_pos = self.move_pos(self.tail_pos, -1, 1)
        elif self.head_pos[0] < self.tail_pos[0] and self.head_pos[1] < self.tail_pos[1]:
            self.tail_pos = self.move_pos(self.tail_pos, -1, -1)
        else:
            pass
        self.cell(self.tail_pos).tail_visited = True
    
    def cell_char(self, cell_pos):
        if self.head_pos == cell_pos:
            return 'H'
        elif self.tail_pos == cell_pos:
            return 'T'
        elif self.start_pos == cell_pos:
            return 's'
        elif self.cell(cell_pos).tail_visited:
            return '#'
        else:
            return '.'
    
    def dump(self):
        print('============')
        for y in range(GRID_HEIGHT):
            print(''.join(self.cell_char((x, y)) for x in range(GRID_WIDTH)))
    
    @property
    def count_visited(self):
        visited = 0
        for row in self.rows:
            for c in row:
                if c.tail_visited:
                    visited += 1
        return visited

def do_sample_p1():
    #breakpoint()
    g = Grid()
    for move in sample_input():
        d, num = move.split()
        g.move(d, int(num))
        #g.dump()
    return g.count_visited

def p1():
    g = Grid()
    for move in read_input():
        d, num = move.split()
        g.move(d, int(num))
    return g.count_visited

def p2():
    return None

print(do_sample_p1())
print(p1())
print(p2())