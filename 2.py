input = '2-input.txt'

def choice_score(choice):
    if choice == 'X':
        return 1
    elif choice == 'Y':
        return 2
    return 3

def choice_score2(choice):
    if choice == 0:
        return 1
    elif choice == 1:
        return 2
    return 3

def outcome_score(them, us):
    them = ord(them) - ord('A')
    us = ord(us) - ord('X')
    return outcome_score_impl(them, us)
    
def outcome_score_impl(them, us):
    if them == us:
        return 3
    if them == 0:
        return 6 if us == 1 else 0
    if them == 1:
        return 6 if us == 2 else 0
    if them == 2:
        return 6 if us == 0 else 0

def get_score(them, us):
    return choice_score(us) + outcome_score(them, us)

def p1():
    score = 0
    for line in open(input, 'r').readlines():
        them, us = line.strip().split(' ')
        score += get_score(them, us)
    print(score)

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

def get_our_move(them, result):
    if result == DRAW:
        return them
    if result == WIN:
        if them == 0:
            return 1
        if them == 1:
            return 2
        return 0
    if them == 0:
        return 2
    if them == 1:
        return 0
    return 1

def p2():
    score = 0
    for line in open(input, 'r').readlines():
        them, result = line.strip().split(' ')
        them = ord(them) - ord('A')
        us = get_our_move(them, result)
        score += choice_score2(us) + outcome_score_impl(them, us)
    print(score)

p2()