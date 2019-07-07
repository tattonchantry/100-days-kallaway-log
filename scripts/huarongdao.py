# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:50:57 2019

@author: Brodie

Huarongdao is a well-known game in China. The purpose of this game is to move
the Cao Cao block out of the board.

Acme is interested in this game, and he invents a similar game. There is a
N*M board. Some blocks in this board are movable, while some are fixed. There
is only one empty position. In one step, you can move a block to the empty
position, and it will take you one second. The purpose of this game is to move
the Cao Cao block to a given position. Acme wants to finish the game as fast
as possible.

But he finds it hard, so he cheats sometimes. When he cheats, he spends K
seconds to pick a block and put it in an empty position. However, he is not
allowed to pick the Cao Cao block out of the board.

Note

Immovable blocks cannot be moved while cheating.
A block can be moved only in the directions UP, DOWN, LEFT or RIGHT.
Input Format

The first line contains four integers N, M, K, Q separated by a single space.
N lines follow.

Each line contains M integers 0 or 1 separated by a single space. If the jth
integer is 1, then the block in ith row and jth column is movable. If the jth
integer is 0 then the block in ith row and jth column is fixed. Then Q lines
follows, each line contains six integers EXi, EYi, SXi, SYi, TXi, TYi separated
by a single space. The ith query is the Cao Cao block is in row SXi column SYi,
the exit is in TXi, TYi, and the empty position is in row EXi column EYi. It is
guaranteed that the blocks in these positions are movable. Find the minimum
seconds Acme needs to finish the game. If it is impossible to finish the game,
you should answer -1.

Constraints

N,M ≤ 200
1 ≤ Q ≤ 250
10 ≤ K≤ 15
1 ≤ EXi, SXi, TXi≤ N
1 ≤ EYi, SYi,TYi ≤ M

Output Format

You should output Q lines, i-th line contains an integer which is the answer
to i-th query.

Sample Input
5 5 12 1
1 1 1 1 1
1 1 1 1 1
0 1 1 1 1
1 1 1 1 1
0 1 0 1 1
1 5 4 3 4 1

Sample Output
20

Explanation

Move the block in (1, 4) to (1, 5);
Move the block in (1, 3) to (1, 4);
Move the block in (1, 2) to (1, 3);
Move the block in (2, 2) to (1, 2);
Move the block in (3, 2) to (2, 2);
Move the block in (4, 2) to (3, 2);
Move the block in (4, 3) to (4, 2);
Move the block in (4, 1) to (4, 3) by cheating;
Move the block in (4, 2) to (4, 1).

So, 1 + 1 + 1 + 1 + 1 + 1 + 1 + 12 + 1 = 20.
"""
import copy

def WhichDir(d, empty_or_chip='E'):
    """
    Creates a vector of which way I want to move. Either the chip towards the
    goal, or the empty cel towards the next chip move
    Takes:
        Dictionary of all variables
        **kwargs:
            empty_or_chip as 'E' or 'C'
                default is 'E', meaning where I want to move the empty space to
                'C' is where I want to move the chip to
    """
    wd = []
    if empty_or_chip == 'E':
        vr = d['empty'] # place I am coming from
        f = d['wiw'] # place I am going towards
    elif empty_or_chip == 'C':
        vr = d['chip']
        f = d['goal']
    # Y direction
    if vr[0] < chip[0]:
        wd.append(goal[0] - chip[0])
    else:  # I need the first coordinate to be pos
        wd.append(chip[0] - goal[0])
    # X direction
    if goal[1] < chip[1]:
        wd.append(goal[1] - chip[1])
    else:
        wd.append(chip[1] - goal[1])
    return wd


def MakeVB(d):
    vb = copy.deepcopy(d['oboard'])
    vb[d['empty'][0]][d['empty'][1]] = 'E'
    vb[d['chip'][0]][d['chip'][1]] = 'C'
    vb[d['goal'][0]][d['goal'][1]] = 'G'
    return vb


def CanI(d):
    """
    Decides if the coordinates I want to move the chip to are
    empty, full, or immovable.
    Returns:
        'E' for empty
        'F' for full
        'I' for immovable
    """
    if d['vboard'][wiw[0]][wiw[1]] == empty:
        yn = 'E'
    elif d['vboard'][wiw[0]][wiw[1]] == 1:
        yn = 'F'
    elif d['oboard'][wiw[0]][wiw[1]] == 0:
        yn = 'I'
    return yn


def WhrIWant(d):
    """
    Gives the coordinates of where I want to move the chip to.
    """
    wiw = []

    # Y direction moves
    if wd[0] == 0:
        wiw.append(int(chip[0]))
    elif wd[0] > 0:
        wiw.append(int(chip[0]) + 1)
    elif wd[0] < 0:
        wiw.append(int(chip[0]) - 1)

    # X direction moves
    if wd[1] == 0:
        wiw.append(chip[1])
    elif wd[1] > 0:
        wiw.append(int(chip[1]) + 1)
    elif wd[1] < 0:
        wiw.append(int(chip[1]) - 1)

    return wiw


def FsRte():
    route_nums = []
    lengths = []
    routes = []
    cntr = 1
    # find dir
    more = True
    while more:
        new_route_list = []
        move_vec = [(empty[0] - wiw[0]), (empty[1] - wiw[1])]
        if move_vec[0] == 0:
            y_e_move = 0
        elif move_vec[0] >= 0 and board[empty[0] + 1, empty[1]] != 0:
            new_route_list.append(board[empty[0] + 1, empty[1]])
        routes.append(new_route_list)
    move_vec = [(empty[0] - wiw[0]), (empty[1] - wiw[1])]
    pass
"""
[1, 1, 1, 1, 'E']
[1, 1, 1, 1, 1]
[0, 1, 1, 1, 1]
['G', 1, 'C', 1, 1]
[0, 1, 0, 1, 1]
"""


def MvEm():
    # reset empty
    board[empty[0]][empty[1]] = 1
    board[
    pass


def huarongdao(k, board, queries):
    huge_dict = {}
    huge_dict['oboard'] = board
    huge_dict['answer'] = 0
    huge_dict['empty'] = [queries[0] - 1, queries[1] - 1]
    huge_dict['chip'] = [queries[2] - 1, queries[3] - 1]
    huge_dict['goal'] = [queries[4] - 1, queries[5] - 1]

    # build a visual board that I can change and keep variables straight
    # in my head
    huge_dict['vboard'] = MakeVB(huge_dict)

    # which direction to go
    huge_dict['wd'] = WhichDir(huge_dict, empty_or_chip='C')

    # Where I want to move
    huge_dict['wiw'] = WhrIWant(huge_dict)

    # can I go that way?
    huge_dict['ci'] = CanI(huge_dict)

    while not ci:
        wiw = WhrIWant()
        ci = CanI(wiw, empty, board)
        # Calculate fastest route
        if not ci:
            fr = FsRte(wiw, board)
            # Move them
            board, answer = MvEm(fr, answer, board)
        elif ci:
            board, answer = MvEm(fr, answer, board)
    return answer


board = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 1, 0, 1, 1]]

k = 12

queries = [1, 5, 4, 3, 4, 1]
# 1, 5 is the empty spot
# 4, 3 is the chip
# 4, 1 is the goal

answer = huarongdao(k, board, queries)
print(answer)