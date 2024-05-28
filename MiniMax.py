#initially min max starts with max function
def minimax(tree, terminal_nodes, node,isMax = True):          
    #if terminal node return its value and node in a list
    if node in terminal_nodes.keys():                           
        return terminal_nodes[node], [node]
    
    #if max function initial value is negative infinity
    #if min function initial value to infinity
    if isMax:                                                   
        val = float('-inf')
    else :                                                      
        val = float('inf')

    path = []
    for i in tree[node]:
        #solving recursively and alternating between min and max in minimax per depth
        temp_val, temp_path = minimax(tree, terminal_nodes,i,not isMax) 

        #if max evaluate the max value out of all
        #if min evaluate the min value out of all
        if isMax:                                               
            val = max(val, temp_val)
        else :                                                  
            val = min(val, temp_val)

        #selecting path which consist of optimal value
        if val == temp_val:                                     
            path = temp_path

    #adding current node to the path
    path.insert(0, node)
    #returning optimal value with optimal path
    return val, path

terminal_nodes = {
    'Q': 5,
    'R': 2,
    'S': 6,
    'T': -1,
    'U': 1,
    'V': 7,
    'W': 9,
    'X': -4,
}

tree = {
    'I': ['J', 'K'],
    'J': ['L', 'M'],
    'K': ['N', 'O'],
    'L': ['Q', 'R'],
    'M': ['S', 'T'],
    'N': ['U', 'V'],
    'O': ['W', 'X'],
}

val, path = minimax(tree, terminal_nodes, 'I')
print("Optimal Solution : ",val)
print(path)