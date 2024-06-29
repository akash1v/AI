def BFS(grp, root_key, goal_key):
    queue = [root_key]
    visited = []

    while queue:
        key = queue.pop(0)       #first in first out

        if key == goal_key:      #found the goal key
            return True

        nbr = grp[key]           # neighbours of the exploring key
        for i in nbr:
            if i not in visited and i not in queue:
                queue.append(i)  
        
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

    print(BFS(graph, 'B', 'T'))
    print(BFS(graph, 'B', 'K'))