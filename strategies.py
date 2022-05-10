from queue import PriorityQueue

import node
import time
import input_output as io


MAX_DEPTH = 22
TARGET_BOARD = []


def target_state(w: int, k: int):
    target_board = []
    for y in range(w):
        row = []
        for x in range(k):
            row.append(y * k + x + 1)
        target_board.append(row)
    target_board[w - 1][k - 1] = 0
    global TARGET_BOARD
    TARGET_BOARD = node.State(target_board)


def goal_reached(board: node.State):
    return board == TARGET_BOARD


def bfs(start_time: float, board: node.State, additional_param: []):
    visited_states = 1
    processed_states = 0
    current_node = node.Node(board, None, None, additional_param)
    open_states = []
    closed_states = set()
    max_depth = 0
    open_states.append(current_node)

    while open_states:
        v = open_states.pop(0)
        processed_states += 1
        max_depth = max(max_depth, v.depth)

        if goal_reached(v.state):
            return io.Output(
                v.get_solution(),
                visited_states,
                processed_states,
                max_depth,
                time.process_time() - start_time
            )

        if v not in closed_states:
            closed_states.add(v)
            neighbours = v.get_neighbours()
            for neighbour in neighbours:
                if neighbour not in closed_states:
                    open_states.append(neighbour)
                    visited_states += 1
    return False


def dfs(start_time: float, board: node.State, additional_param: []):
    visited_states = 1
    processed_states = 0
    current_node = node.Node(board, None, None, additional_param)
    open_states = []
    closed_states = set()
    max_depth = 0
    open_states.append(current_node)

    while open_states:
        v = open_states.pop(-1)
        processed_states += 1
        max_depth = max(max_depth, v.depth)

        if v not in closed_states:
            closed_states.add(v)

            if goal_reached(v.state):
                return io.Output(
                    v.get_solution(),
                    visited_states,
                    processed_states,
                    max_depth,
                    time.process_time() - start_time
                )

            if v.depth < MAX_DEPTH:
                neighbours = v.get_neighbours()
                if neighbours is not None:
                    neighbours.reverse()
                    for neighbour in neighbours:
                        if neighbour not in closed_states:
                            open_states.append(neighbour)
                            visited_states += 1
    return False


class ElementDekorator:
    def __init__(self, element_id, node_object, distance):
        self.element_id = element_id
        self.node_object = node_object
        self.distance = distance

    def __le__(self, other):
        return self.distance <= other.distance and self.element_id <= other.node_id

    def __lt__(self, other):
        return self.distance < other.distance and self.element_id < other.node_id


def astr(start_time: float, board: node.State, heuristic):
    visited_states = 1
    processed_states = 0
    current_node = node.Node(board, None, None)
    open_states = PriorityQueue()
    closed_states = set()
    max_depth = 0
    open_states.put(ElementDekorator(processed_states, current_node, heuristic(current_node.state)))

    while open_states:
        v = open_states.get().node

        if v in closed_states:
            continue

        processed_states += 1
        max_depth = max(max_depth, v.depth)

        if goal_reached(v.state):
            return io.Output(
                v.get_solution(),
                visited_states,
                processed_states,
                max_depth,
                time.process_time() - start_time
            )

        closed_states.add(v)
        for neighbour in v.get_neighbours():
            if neighbour not in closed_states:
                distance = neighbour.depth + heuristic(neighbour)
                open_states.put(ElementDekorator(processed_states, neighbour, distance))
                visited_states += 1
    return False

