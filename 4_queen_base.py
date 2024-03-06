from search import Problem, Trial_Error


def convert_state_to_list(state_tuple):
    return [list(x) for x in state_tuple]


def convert_state_to_tuple(state_list):
    return [tuple(x) for x in state_list]


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


class FourQueensProblem(Problem):
    def __init__(self):
        # Fill out the __init__ call with only the initial state of the problem (in tuple of tuples format)
        # Represent 4*4 size chess board where 0=empty, 1=queen, 2=in conflict
        super().__init__(((0, 0, 0, 0),
                         (0, 0, 0, 0),
                         (0, 0, 0, 0),
                         (0, 0, 0, 0)))

    def actions(self, state):
        # Return a list of possible actions in "o i j" format where
        # i is the row (from 1 to 4) and j is the column (from 1 to 4)
        acts = []
        # Find an empty space
        for i in range(4):
            for j in range(4):
                if state[i][j] == 0:
                    acts.append(f"o {i + 1} {j + 1}")
        return acts

    def result(self, state, action):
        # Return with the new state of the result of the action parameter used in the state parameter.
        # Tip: don't forget to convert state to list of lists and then convert the result back to tuple of tuples
        i, j = int(action.split(" ")[1]) - 1, int(action.split(" ")[2]) - 1 # row and column of queen
        new_state = convert_state_to_list(state)

        for k in range(4): # use for row
            for l in range(4): # use for column
                if k == i and l == j: # identify state[i][j] based on action input
                    new_state[k][l] = 1
                # if it's not the space we are going to put the queen not (k == i and l == j),
                # and vertical line, horizontal line, diagonal lines are selected by
                # k == i, l == j, abs(i - k) == abs(j - l) respectively
                # Those position can't be placed by another queen anymore
                elif not (k == i and l == j) and (k == i or l == j or abs(i - k) == abs(j - l)):
                    new_state[k][l] = 2
                # no need for empty space as all spaces are 0 (empty) by default
        return convert_state_to_tuple(new_state)

    def goal_test(self, state):
        # For a given state parameter check if it is a goal state.
        # Tip 1: don't forget conversions; Tip 2: you can use any() or all() for easier implementation
        bool_state = convert_state_to_list(state)

        for i in range(4):
            for j in range(4):
                # if there is a queen, value on the space becomes 1
                bool_state[i][j] = state[i][j] == 1
        # if each row has a queen, return true. Otherwise, it returns false.
        return all([any(bool_state[i]) for i in range(4)])


def main():
    # Test every method that you created: actions, result, goal_test.
    # Also try to solve the problem using the Trial_Error method (found in the search library)
    f_queen = FourQueensProblem()

    my_state = ((0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0))
    print(convert_state_to_list(my_state))

    print(len(f_queen.actions(my_state)))

    print_matrix(f_queen.result(my_state, "o 4 4"))

    my_goal_state = ((0, 1, 0, 0),
                     (0, 0, 0, 1),
                     (1, 0, 0, 0),
                     (0, 0, 1, 0))
    print()
    print_matrix(my_goal_state)
    print(f_queen.goal_test(my_goal_state))

    print()
    print(f_queen.goal_test(f_queen.result(my_state, "o 4 4")))

    print()
    print("Trying to solve with Trial Error method")
    print(Trial_Error(f_queen))


main()
