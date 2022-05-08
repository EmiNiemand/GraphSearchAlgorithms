import strategies
import time
import node
import input_output as io

class BoardValidationException(Exception):
    pass


def validate_board(board):
    correct_elements = set(range(len(board) * len(board[0])))
    for row in range(len(board)):
        for element in board[row]:
            if element not in correct_elements:
                raise BoardValidationException("Board contains wrong elements")
            correct_elements.discard(element)


def main():
    input_args = io.get_input()
    input_args.validate()
    #read
    with open(input_args.source_file_name, "r") as file:
        if not file.readable():
            raise Exception("Cannot open the file: " + file.name)

        w, k = [int(x) for x in next(file).split()]  # read first line
        board = []
        for line in file:  # read rest of lines
            board.append([int(x) for x in line.split()])

    print(board)
    validate_board(board)
    strategies.target_state(w, k)

    board = node.State(board)

    output = None
    if input_args.acronym == "bfs":
        start_time = time.process_time()
        output = strategies.bfs(start_time, board, list(input_args.additional_param))
    elif input_args.acronym == "dfs":
        start_time = time.process_time()
        output = strategies.dfs(start_time, board, list(input_args.additional_param))
    elif input_args.acronym == "astr":
        start_time = time.process_time()
        output = strategies.astr(start_time, board, list(input_args.additional_param))

    #Save result
    with open(input_args.save_file_name, "w+") as file:
        if output is False:
            file.write("-1")
        else:
            file.write(output.get_result())

    #Save result additional information
    with open(input_args.additional_file_name, "w+") as file:
        if output is False:
            file.write("-1")
        else:
            file.write(output.get_result_additional_info())


if __name__ == '__main__':
    main()

