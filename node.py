class StateValueError(ValueError):
    pass

class State:
    target_states = {}

    def __init__(self, elements):
        self.elements = elements

    def __eq__(self, other):
        for row in range(len(self.elements)):
            for column in range(len(self.elements[row])):
                if self.elements[row][column] != other.elements[row][column]:
                    return False
        return True

    def validate(self):
        correct_elements = set(range(len(self.elements) * len(self.elements[0])))
        for row in range(len(self.elements)):
            for element in self.elements[row]:
                if element not in correct_elements:
                    raise StateValueError("Board contains wrong elements")
                correct_elements.discard(element)

    def get_elements(self):
        return self.elements

