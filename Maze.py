import numpy as np

class Maze:
    def __init__(self, filename):

        with open(filename, 'r') as f:
            contents = f.read()
        
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one starting point")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one ending point")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(i) for i in contents)
        self.maze = np.ndarray(shape= (self.height, self.width), dtype=bool)

        for i in range(self.height):
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        self.maze[i][j] = True
                    elif contents[i][j] == "B":
                        self.end = (i, j)
                        self.maze[i][j] = True
                    elif contents[i][j] == " ":
                        self.maze[i][j] = True
                    else:
                        self.maze[i][j] = False
                except IndexError:
                    self.maze[i][j] = True

    def print(self, state_explored = None):
        print()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.end:
                    print("B", end="")
                elif state_explored and (i, j) in state_explored:
                    print("*", end="")
                elif self.maze[i][j]:
                    print(" ", end="")
                else:
                    print("█", end="")
            print()
        print()

    def neighbours(self, state = (-1, -1)):

        row, col = state
        operations = [
            (row, col + 1), #right
            (row + 1, col), #down
            (row, col - 1), #left
            (row - 1, col), #up
        ]

        nbrs = []
        for (r, c) in operations:
            if  0 <= r < self.height and 0 <= c < self.width and self.maze[r][c]:
                nbrs.append((r, c))

        return nbrs
