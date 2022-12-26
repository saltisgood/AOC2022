from dataclasses import dataclass
from typing import Dict, List, Any

input = '7-input.txt'

def read_input():
    for line in open(input, 'r').readlines():
        yield line.strip()

@dataclass
class File:
    name: str
    size: int

@dataclass
class Dir:
    name: str
    files: Dict[str, File]
    dirs: Dict[str, Any]
    _size: int | None = None

    def __init__(self, name):
        self.name = name
        self.files = {}
        self.dirs = {}

    def add_file(self, f: File):
        if f.name not in self.files:
            self.files[f.name] = f
    
    def add_dir(self, name: str):
        if name not in self.dirs:
            self.dirs[name] = Dir(name=name)
        return self.dirs[name]
    
    def walk_dirs(self, handler):
        for d in self.dirs.values():
            handler(d)
            d.walk_dirs(handler)
    
    @property
    def size(self):
        if self._size is None:
            sz = sum(f.size for f in self.files.values())
            sz += sum(d.size for d in self.dirs.values())
            self._size = sz
        return self._size

@dataclass
class Filesystem:
    root: Dir
    current_pos: List[Dir]
    current_dir = Dir

    def __init__(self):
        self.root = Dir(name='/')
        self.move_to_root()
    
    def move_to_root(self):
        self.current_pos = [self.root]
        self.current_dir = self.root
    
    def move_up(self):
        self.current_pos.pop()
        self.current_dir = self.current_pos[-1]
    
    def move_down(self, name):
        new_dir = self.current_dir.add_dir(name)
        self.current_pos.append(new_dir)
        self.current_dir = new_dir
    
    def walk_dirs(self, handler):
        self.root.walk_dirs(handler)
    
    @property
    def size(self):
        return self.root.size

def parse_commands(lines):
    f = Filesystem()
    for l in lines:
        if l[0] == '$':
            if l == '$ cd /':
                f.move_to_root()
            elif l == '$ cd ..':
                f.move_up()
            elif l.startswith('$ cd '):
                f.move_down(l[5:])
        else:
            if l.startswith('dir '):
                f.current_dir.add_dir(l[4:])
            else:
                size, name = l.split(' ')
                f.current_dir.add_file(File(name, int(size)))

    return f

@dataclass
class Traverser:
    total: int = 0

    def __call__(self, d: Dir):
        if d.size <= 100000:
            self.total += d.size

def p1():
    f = parse_commands(read_input())
    t = Traverser()
    f.walk_dirs(t)
    return t.total

@dataclass
class TraverserP2:
    min_size: int
    size_dir: int = 9999999999999

    def __call__(self, d: Dir):
        if d.size >= self.min_size and d.size < self.size_dir:
            self.size_dir = d.size

def p2():
    f = parse_commands(read_input())
    total_sz = f.size
    required = 30000000
    avail = 70000000 - total_sz
    missing = required - avail
    t = TraverserP2(min_size=missing)
    f.walk_dirs(t)
    return t.size_dir

def sample_input():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

def do_sample_p1():
    breakpoint()
    f = parse_commands(sample_input())
    t = Traverser()
    f.walk_dirs(t)
    print(t.total)

def do_sample_p2():
    breakpoint()
    f = parse_commands(sample_input())
    total_sz = f.size
    required = 30000000
    avail = 70000000 - total_sz
    missing = required - avail
    t = TraverserP2(min_size=missing)
    f.walk_dirs(t)
    print(t.size_dir)

#do_sample()
do_sample_p2()
print(p1())
print(p2())