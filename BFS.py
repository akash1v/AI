from Maze import Maze
class Queue:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)
    
    def pop(self):
        return self.list.pop(0)
    
    def search(self, val):
        if val in self.list:
            return True
        return False

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False
    
def BFS(maze):
    frontier = Queue()
    explored = []

    frontier.push(maze.start)

    while True:
        if frontier.isEmpty():
            raise Exception("No Solution")
        
        state = frontier.pop()
        
        if state == maze.end:
            break
        
        neighbours = maze.neighbours(state)
        for nbr in neighbours:
            if nbr not in explored and not frontier.search(nbr):
                frontier.push(nbr)
        
        explored.append(state)
    
    return explored
        

try :
    maze = Maze('maze.txt')
    solution = BFS(maze)
    print("Solution of maze : ")
    maze.print(solution)
except Exception as e:
    print(e)
