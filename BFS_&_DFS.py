import sys

import numpy as np


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def push(self, state):
        self.frontier.append(state)

    def pop(self):
        i = self.frontier[-1]
        self.frontier.pop(-1)
        return i

    def empty(self):
        return len(self.frontier) == 0


class QueueFrontier(StackFrontier):
    def pop(self):
        i = self.frontier[0]
        self.frontier.pop(0)
        return i


class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one starting point")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one ending point")

        content_inlines = contents.splitlines()

        self.height = len(content_inlines)
        self.width = max(len(i) for i in content_inlines)

        self.maze = np.ndarray(shape=(self.height, self.width), dtype=bool)
        self.solution = []            # write a solution in here
        self.state_explored = []

        for i in range(self.height):
            for j in range(self.width):
                try:
                    if content_inlines[i][j] == "A":
                        self.start = (i, j)
                        self.maze[i][j] = True
                    elif content_inlines[i][j] == "B":
                        self.end = (i, j)
                        self.maze[i][j] = True
                    elif content_inlines[i][j] == " ":
                        self.maze[i][j] = True
                    else:
                        self.maze[i][j] = False
                except IndexError:
                    self.maze[i][j] = True

    def print(self):
        print()
        for i in range(self.height):
            for j in range(self.width):
                if not self.maze[i][j]:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.end:
                    print("B", end="")
                elif (i, j) in self.state_explored:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbor(self, state):
        row, col = state
        operations = [
            (row-1, col),       # up
            (row+1, col),       # down
            (row, col-1),       # left
            (row, col+1)        # right
        ]
        neighbors = []

        for r, c in operations:
            if 0 <= r < self.height and 0 <= c < self.width and self.maze[r][c]:
                neighbors.append((r, c))
        return neighbors

    def solve(self, ftype):

        frontier = None
        self.state_explored = []

        if ftype == "stack":
            frontier = StackFrontier()
        elif ftype == "queue":
            frontier = QueueFrontier()

        frontier.push(self.start)

        while True:
            if frontier.empty():
                raise Exception("No solution")

            i = frontier.pop()

            if i == self.end:
                break

            neighbors_of_i = self.neighbor(i)
            for state in neighbors_of_i:
                if state not in self.state_explored:
                    frontier.push(state)
            self.state_explored.append(i)


m = Maze(sys.argv[1])
print("Maze:")
m.print()

print("Solving using Depth First Search Algorithm ...")
m.solve(ftype="stack")
print("States Explored:", len(m.state_explored))
print("Solution:")
m.print()

print("Solving using Breadth First Search Algorithm ...")
m.solve(ftype="queue")
print("States Explored:", len(m.state_explored))
print("Solution:")
m.print()
