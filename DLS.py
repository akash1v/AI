def DLS(grp, root_key, goal_key, depth):

    if depth < 0:                           #checking depth
        return False
    if root_key == goal_key:                #goal key found
        return True
    
    childrens = grp[root_key]                     #childrens of the exploring key

    for child in childrens:                       #exploring each children with a reduced depth
        if DLS(grp, child,goal_key, depth - 1):
            return True
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
    depth = DLS(graph, 'B', 'T', 3)
    print(depth)