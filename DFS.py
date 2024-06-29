def DFS(grp, root_key, goal_key):
    stack = [root_key]
    visited = []

    while stack:
        key = stack.pop()         #last in first out
        
        if key == goal_key:       #goal key found
            return True

        nbr = grp[key]            # neighbours of the exploring key        
        for i in nbr:
            if i not in visited and i not in stack:
                stack.append(i) 
        
        visited.append(key)
    return False


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

    print(DFS(graph, 'B', 'T'))
    print(DFS(graph, 'B', 'K'))