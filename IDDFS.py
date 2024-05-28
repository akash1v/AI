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

def IDDFS(grp, root_key, goal_key, max_depth):
    for i in range(0, max_depth + 1):
        print(f"\nDepth : {i}")
        opened = [root_key]
        closed = []
        result = DLS(grp, root_key, goal_key, i, opened, closed)
        print(f"Open List : {*opened,},        Close List : {*closed,}")    
        if result:
            print("Goal key found")
            break
    return False

        
def DLS(grp, root_key, goal_key, depth, opened, closed):

    if depth < 0:
        return
    if root_key == goal_key:
        return True
    
    print(f"Open List : {*opened,},        Close List : {*closed,}")    
    key = opened.pop()
    closed.append(key)
    nbr = grp[key]
    
    if depth > 0:
        for i in nbr[::-1]:
            opened.append(i)
        for i in nbr[::-1]:
            if DLS(grp, i,goal_key, depth - 1, opened, closed) == True:
                return True
    return False

IDDFS(graph, 'B', 'T', 3)