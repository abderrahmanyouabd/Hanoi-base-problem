from search import Problem, Trial_Error


class Cup3(Problem):
    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        # if you write ((4, 1, 0), (4, 0, 1)) instead, Trial_Error() doesn't work
        super().__init__((5, 0, 0), [(4, 1, 0), (4, 0, 1)])

        self.H1 = [0, 1, 2, 3, 4, 5] # Possible value cup1 may take
        self.H2 = [0, 1, 2, 3] # Possible value cup2 may take
        self.H3 = [0, 1, 2] # Possible value cup3 may take

        self.H = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3], [0, 1, 2]] # Possible state of 3 cups

    def actions(self, state):
        """Return all the actions that can be executed in the given
        state"""
        acts = []
        cup1, cup2, cup3 = state # state is tuple, cup1 = state[0], cup2 = state[1],...
        # (cup1, cup2, cup3) = state comes in the same result

        if cup1 > 0 and cup2 < max(self.H2): # cup1 isn't empty and cup2 is less than 3
            acts.append("o 1 2")
        if cup1 > 0 and cup3 < max(self.H3): # cup1 isn't empty and cup3 is less than 2
            acts.append("o 1 3")
        if cup2 > 0 and cup1 < max(self.H1):
            acts.append("o 2 1")
        if cup2 > 0 and cup3 < max(self.H3):
            acts.append("o 2 3")
        if cup3 > 0 and cup1 < max(self.H1):
            acts.append("o 3 1")
        if cup3 > 0 and cup2 < max(self.H2):
            acts.append("o 3 2")
        return acts

    def actions2(self, state):
        acts = []

        for i in range(1, 4):
            for j in range(1, 4):
                if i != j: # can't choose the same cup as we want to move water from one to another
                    # from-cup i not empty and to-cup j has capacity
                    if state[i-1] > 0 and state[j-1] < max(self.H[j-1]):
                        acts.append(f"o {i} {j}")
        return acts

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. Assume that the action is one of
        self.actions(state)."""
        cup1, cup2, cup3 = state
        if action == "o 1 2":
            # amount of water to move = either cup1 or cup2's capacity
            m = min(cup1, max(self.H2) - cup2)
            return cup1 - m, cup2 + m, cup3 # multiple return values are treated as a tuple
        if action == "o 1 3":
            m = min(cup1, max(self.H3) - cup3)
            return cup1 - m, cup2, cup3 + m
        if action == "o 2 1":
            m = min(cup2, max(self.H1) - cup1)
            return cup1 + m, cup2 - m, cup3
        if action == "o 2 3":
            m = min(cup2, max(self.H3) - cup3)
            return cup1, cup2 - m, cup3 + m
        if action == "o 3 1":
            m = min(cup3, max(self.H1) - cup1)
            return cup1 + m, cup2, cup3 - m
        if action == "o 3 2":
            m = min(cup3, max(self.H2) - cup2)
            return cup1, cup2 + m, cup3 - m

    def result2(self, state, action):
        from_cup = int(action.split(" ")[1]) # select from-cup in action i.g. 1 in "o 1 2"
        to_cup = int(action.split(" ")[2]) # select from-cup in action i.g. 2 in "o 1 2"
        v = min(state[from_cup - 1], max(self.H[to_cup - 1]) - state[to_cup - 1])

        new_state = list(state) # convert tuple to list to modify elements

        new_state[from_cup - 1] = state[from_cup - 1] - v
        new_state[to_cup - 1] = state[to_cup - 1] + v

        return tuple(new_state)


def main():
    a = Cup3()
    c = Cup3()

    print(a.actions((5, 0, 0)))  # Initial actions we can do
    print(a.result((5, 0, 0), "o 1 2"))

    print(c.actions2((5, 0, 0))) # Initial actions we can do
    print(c.result2((5, 0, 0), "o 1 2"))

    print(Trial_Error(c))


main()
