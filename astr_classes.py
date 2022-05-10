from math import floor

import strategies as strat


class Hamming:
    def __call__(self, neighbour):
        hamming_distance = 0
        for y in range(len(neighbour)):
            for x in range(len(neighbour[y])):
                if neighbour[y][x] != strat.TARGET_BOARD[y][x] and neighbour[y][x] != 0:
                    hamming_distance += 1
        return hamming_distance


class Manhattan:
    def __call__(self, neighbour):
        manhattan_distance = 0
        for y in range(len(neighbour)):
            for x in range(len(neighbour[y])):
                if neighbour[y][x] != strat.TARGET_BOARD[y][x] and neighbour[y][x] != 0:
                    x_pos = (neighbour[y][x] - 1) % len(strat.TARGET_BOARD)
                    y_pos = floor((neighbour[y][x] - 1) / len(strat.TARGET_BOARD))
                    manhattan_distance += abs(x - x_pos) + abs(y - y_pos)
        return manhattan_distance

