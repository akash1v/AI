tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['M'],
    'G': ['N', 'O'],
    'H': ['P'],
    'I': ['Q'],
    'J': ['R', 'S'],
    'K': ['T1', 'T2'],
    'L': ['T3', 'T4', 'T5'],
    'M': ['T6'],
    'N': ['T7'],
    'O': ['T8', 'T9'],
    'P': ['T10'],
    'Q': ['T11'],
    'R': ['T12', 'T13'],
    'S': ['T14'],
}

terminal_nodes = {
    'T1' : 5,    
    'T2' : 6,    
    'T3' : 7,    
    'T4' : 4,    
    'T5' : 5,    
    'T6' : 3,    
    'T7' : 6,    
    'T8' : 6,    
    'T9' : 9,    
    'T10' : 7,    
    'T11' : 5,    
    'T12' : 9,    
    'T13' : 8,    
    'T14' : 6,
}

#initially min max starts with max function
def minimax_alpha_beta(
    tree, terminal_nodes, node,
    alpha = float('-inf'), beta = float('inf'), isMax = True
    ):          
    
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
        #solving recursively and alternating between min and max in minimax_alpha_beta per depth
        temp_val, temp_path = minimax_alpha_beta(
            tree, terminal_nodes,i,alpha, beta, not isMax
        ) 

        #if the branch is pruned then return the optimal value
        if temp_val == None:
            path.insert(0, node)
            return val, path
        
        #if max evaluate the max value out of all
        #if min evaluate the min value out of all
        if isMax:                                               
            val = max(val, temp_val)
            alpha = max(alpha, temp_val)
        else :                                                  
            val = min(val, temp_val)
            beta = min(beta, temp_val)

        #pruning if possible
        if beta <= alpha:
            return None,None

        #selecting path which consist of optimal value
        if val == temp_val:                                     
            path = temp_path

    #adding current node to the path
    path.insert(0, node)
    #returning optimal value with optimal path
    return val, path

val, path = minimax_alpha_beta(tree, terminal_nodes, 'A')
print("Optimal Solution : ",val)
print(path)