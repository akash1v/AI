from DLS import DLS

def IDDFS(grp, root_key, goal_key, max_depth):
    for i in range(0, max_depth + 1):
        if DLS(grp, root_key, goal_key, i):
            return i
    return -1
        

if __name__ == "__main__":
    graph = {
        'B' : ['C', 'N'],
        'C' : ['A', 'Q'],
        'A' : ['M'],
        'Q' : ['R'],
        'N' : ['S'],
        'S' : ['T', 'Z'],
        'M' : [],
        'R' : [],
        'T' : [],
        'Z' : [],
    }

    depth = IDDFS(graph, 'B', 'T', 3)
    print(depth)