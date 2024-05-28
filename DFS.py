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

def DFS(grp, root_key):
    opened = []
    closed = []

    opened.append(root_key)       # root key added

    print(f"Open List : {*opened,},        Close List : {*closed,}")

    while len(opened) != 0:
        key = opened.pop()       
        nbr = grp[key]            # neighbours of the exploring key
        
        for i in nbr:
            if i not in closed and i not in opened:
                opened.append(i) 
        
        closed.append(key)
        print(f"Open List : {*opened,},         Close List : {*closed,}")

DFS(graph, 'B')