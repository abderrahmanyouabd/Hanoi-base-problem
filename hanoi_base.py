import math
from collections import deque


class Hanoi:
    def __init__(self):
        self.initial_state = [{1, 2, 3, 4}, set(), set()]
        self.goal_state = [set(), set(), {1, 2, 3, 4}]

    def actions(self, state):
        acts = []
        inf_set = {math.inf}
        for i in range(3):
            for j in range(3):
                if i != j and state[i]:
                    for k in range(1, 5):
                        if k == min(state[i].union(inf_set)) and (not state[j] or k < min(state[j].union(inf_set))):
                            acts.append(f"o {i + 1} {j + 1} {k}")
        return acts

    def result(self, state, action):
        i, j, k = action.split(' ')[1:]
        from_tower = int(i) - 1
        to_tower = int(j) - 1
        disk_size = int(k)

        new_state = state.copy()
        new_state[from_tower] = state[from_tower].difference({disk_size})
        new_state[to_tower] = state[to_tower].union({disk_size})

        return new_state

    def solve_bread(self):
        state = self.initial_state
        print('Initial State:', state)

        frontier = deque([(tuple(map(frozenset, state)), [])])  # Queue of (state, actions) tuples
        visited_states = set()

        while frontier:
            state, actions = frontier.popleft()

            if state == tuple(map(frozenset, self.goal_state)):
                print('Goal State Reached:', state)
                print('Actions:', actions)
                return

            for action in self.actions(list(map(set, state))):
                new_state = self.result(list(map(set, state)), action)
                if tuple(map(frozenset, new_state)) not in visited_states:
                    visited_states.add(tuple(map(frozenset, new_state)))
                    frontier.append((tuple(map(frozenset, new_state)), actions + [action]))

        print('No solution found.')

    def solve_depth(self):
        state = self.initial_state
        print('Initial State:', state)

        frontier = [(tuple(map(frozenset, state)), [])]  # Stack of (state, actions) tuples
        visited_states = set()

        while frontier:
            state, actions = frontier.pop()

            if state == tuple(map(frozenset, self.goal_state)):
                print('Goal State Reached:', state)
                print('Actions:', actions)
                return

            for action in self.actions(list(map(set, state))):
                new_state = self.result(list(map(set, state)), action)
                if tuple(map(frozenset, new_state)) not in visited_states:
                    visited_states.add(tuple(map(frozenset, new_state)))
                    frontier.append((tuple(map(frozenset, new_state)), actions + [action]))

        print('No solution found.')


def main():
    h = Hanoi()
    h.solve_bread()
    print("-" * 100)
    h.solve_depth()


main()
