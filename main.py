import os.path
import sys


class WrongValueException(ValueError):
    pass

#Class to validate and save the input
class Input:
    def __init__(self, acronym, additional_param, source_file_name, save_file_name, additional_file_name):
        self.acronym = acronym
        self.additional_param = additional_param
        self.source_file_name = source_file_name
        self.save_file_name = save_file_name
        self.additional_file_name = additional_file_name

    def __validate__(self):
        if self.acronym not in ("bfs", "dfs", "astr"):
            raise WrongValueException("Wrong acronym")
        if not set(self.additional_param) == set("LPUD") and \
                self.additional_param not in ("hamm", "manh"):
            raise WrongValueException("Wrong additional param")
        if not os.path.exists(self.source_file_name):
            raise WrongValueException("Given source file does not exist")
        if not self.save_file_name:
            raise WrongValueException("Given save file name is empty")
        if not self.additional_file_name:
            raise WrongValueException("Given additional file name is empty")


#Class that saves the output and
#has 2 different methods of returning the output
#ready to be saved to a file
class Output:
    def __init__(self, solution, visited_states, processed_states, recursion_max_depth, process_time):
        self.solution = solution
        self.visited_states = visited_states
        self.processed_states = processed_states
        self.recursion_max_depth = recursion_max_depth
        self.process_time = process_time

    def get_result(self):
        return f"{self.solution.length}\n" \
                f"{self.solution}"

    def get_result_additional_info(self):
        return f"{self.solution.length}\n" \
                f"{self.visited_states}\n" \
                f"{self.processed_states}\n" \
                f"{self.recursion_max_depth}\n"\
                f"{self.process_time}"


def get_input():
    acronym = sys.argv[1]
    additional_param = sys.argv[2]
    source_file_name = sys.argv[3]
    save_file_name = sys.argv[4]
    additional_file_name = sys.argv[5]
    return Input(
        acronym,
        additional_param,
        source_file_name,
        save_file_name,
        additional_file_name
    )


def main():
    input_args = get_input()

    #read
    with open(input_args.source_file_name, "r") as file:
        if not file.readable():
            raise Exception("Cannot open the file: " + file.name)

        w, k = [int(x) for x in next(file).split()]  # read first line
        array = []
        for line in file:  # read rest of lines
            array.append([int(x) for x in line.split()])
    print(str(w), str(k))
    print(array)

    output = None
    #Save result
    with open(input_args.save_file_name, "w+") as file:
        if not output:
            file.write("-1")
        else:
            file.write(output.get_result())

    #Save additional information
    with open(input_args.additional_file_name, "w+") as file:
        if not output:
            file.write("-1")
        else:
            file.write(output.get_additional_info())


if __name__ == '__main__':
    main()

