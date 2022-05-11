class NoZeroFoundException(Exception):
    pass


class State:
    def __init__(self, elements):
        self.elements = elements

    def __eq__(self, other):
        for y in range(len(self.elements)):
            for x in range(len(self.elements[y])):
                if self.elements[y][x] != other.elements[y][x]:
                    return False
        return True

    def __getitem__(self, item):
        return self.elements[item]

    def __len__(self):
        return len(self.elements)

    def __hash__(self):
        return hash(tuple(map(tuple, self.elements)))


class Node:
    def __init__(self, current_state, parent_node, last_move, sequence=None, depth=0):
        self.state = current_state
        self.last_move = last_move

        if sequence is not None:
            self.sequence = sequence.copy()
        else:
            self.sequence = ['L', 'R', 'U', 'D']

        self.parent = parent_node
        self.depth = depth
        self.zero = self.zero_position()

    def __eq__(self, other):
        return self.state == other.state and self.last_move == other.last_move and self.depth == other.depth

    def __hash__(self):
        return hash(self.state) + hash(self.last_move) + hash(self.depth)

    def get_neighbours(self):
        neighbours = []
        x, y = self.zero
        initial_sequence = self.sequence.copy()

        if self.zero[0] == 0:
            self.sequence.remove('L')
        elif self.zero[0] == len(self.state) - 1:
            self.sequence.remove('R')
        if self.zero[1] == 0:
            self.sequence.remove('U')
        elif self.zero[1] == len(self.state) - 1:
            self.sequence.remove('D')

        for i in range(len(self.sequence)):
            neighbours.append([row[:] for row in self.state])

        if self.sequence is not None:
            index = 0
            for step in self.sequence:
                neighbour = neighbours[index]
                if step == "L":
                    helper = neighbour[y][x - 1]
                    neighbour[y][x - 1] = neighbour[y][x]
                    neighbour[y][x] = helper
                elif step == "R":
                    helper = neighbour[y][x + 1]
                    neighbour[y][x + 1] = neighbour[y][x]
                    neighbour[y][x] = helper
                elif step == "U":
                    helper = neighbour[y - 1][x]
                    neighbour[y - 1][x] = neighbour[y][x]
                    neighbour[y][x] = helper
                elif step == "D":
                    helper = neighbour[y + 1][x]
                    neighbour[y + 1][x] = neighbour[y][x]
                    neighbour[y][x] = helper
                neighbours[index] = Node(State(neighbour), self, step, initial_sequence, self.depth + 1)
                index += 1
        return neighbours

    def get_solution(self):
        solution = []
        if self.last_move is None:
            return solution
        solution.append(self.last_move)
        parent = self.parent
        while parent.last_move:
            solution.append(parent.last_move)
            parent = parent.parent
        solution.reverse()
        return solution

    def zero_position(self):
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                if self.state[y][x] == 0:
                    return tuple((x, y))
        raise NoZeroFoundException("There's no zero in the board")

