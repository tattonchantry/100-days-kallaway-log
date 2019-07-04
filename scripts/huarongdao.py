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


def WhichDir(chip, goal):
    wd = [(goal[0] - chip[0]), (goal[1] - chip[1])]
    return wd


def MakeVB(board, empty, chip, goal):
    vb = board
    vb[empty[0]][empty[1]] = 'E'
    vb[chip[0]][chip[1]] = 'C'
    vb[goal[0]][goal[1]] = 'G'
    return vb


def CanI(chip, wd, empty, board):
    direction = str()
    if wd[0] > 0 and board[chip[0] + 1][chip[1]] == 'E':
        direction = '+x'
    elif wd[1] > 0 and board[chip[0]][chip[1] + 1] == 'E':
        direction = '+y'
    elif wd[0] < 0 and board[chip[0] - 1][chip[1]] == 'E':
        direction = '-x'
    elif wd[1] < 0 and board[chip[0]][chip[1] - 1] == 'E':
        direction = '-y'
    else:
        direction = False
    return direction


def WhrIWant():
    pass


def FsRte():
    pass


def MvEm():
    pass


def huarongdao(k, board, queries):
    answer = 0
    empty = [queries[0] - 1, queries[1] - 1]
    chip = [queries[2] - 1, queries[3] - 1]
    goal = [queries[4] - 1, queries[5] - 1]

    # build a board that is easier for me to visualize
    vb = MakeVB(board, empty, chip, goal)

    # which direction to go
    wd = WhichDir(chip, goal)

    # can I go that way?
    ci = CanI(chip, wd, empty, board)

    while not ci:
        # Where I want to move
        wiwtm = WhrIWant()
        ci = CanI(chip, wd, empty, board)
        # Calculate fastest route
        fr = FsRte()
        # Move them
        mt = MvEm()
    return 5


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