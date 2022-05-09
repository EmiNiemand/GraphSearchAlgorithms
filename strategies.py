import node
import time
import input_output as io


MAX_DEPTH = 20
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


def bfs(start_time: float, board: node.State, additional_param: []) -> []:
    visited_states = 1
    processed_states = 0
    current_node = node.Node(board, None, None, additional_param, 0)
    open_states = []
    closed_states = set()
    max_depth = 0
    open_states.append(current_node)

    while open_states:
        v = open_states.pop(0)
        processed_states += 1
        max_depth = max(max_depth, v.depth)
        if goal_reached(v.state):
            return io.Output(v.get_solution(), visited_states, processed_states,
                             max_depth, time.process_time() - start_time)
        if v not in closed_states:
            closed_states.add(v)
            neighbours = v.get_neighbours()
            for n in neighbours:
                if n not in closed_states:
                    open_states.append(n)
                    visited_states += 1
    return False


def dfs(start_time: float, board: node.State, additional_param: []) -> []:
    return


def astr(start_time: float, board: node.State, additional_param: []) -> []:
    return

