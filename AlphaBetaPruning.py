# initially min max starts with max function
def minimax_alpha_beta(
    tree, leafs, node,
    alpha = float('-inf'), beta = float('inf'), isMax = True
    ):          
    
    # if leaf node return its value and node in a list
    if node in leafs.keys():             
        return leafs[node], [node]
    
    # if max function initial value is negative infinity
    # if min function initial value is positive infinity
    if isMax:                                                   
        value = float('-inf')
    else :                                                      
        value = float('inf')

    path = []
    for i in tree[node]:
        #solving recursively and alternating between min and max in minimax_alpha_beta per depth
        temp_value, temp_path = minimax_alpha_beta(
            tree, leafs,i,alpha, beta, not isMax
        ) 

        # if the branch is pruned then return the optimal value with path
        if temp_value == None:
            path.insert(0, node)
            return value, path
        
        # Evalueuate the max value and its path
        if isMax and (temp_value > value):                            
            value = temp_value              #updating value
            path = temp_path                #updating path
            alpha = temp_value              #updating alpha

        # Evalueuate the min value and its path
        elif not isMax and (temp_value < value):                                                  
            value = temp_value              #updating value
            path = temp_path                #updating path
            beta = temp_value               #updating beta

        # pruning if possible
        if beta <= alpha:
            return None,None


    # if the branch is not pruned add current node to the path
    path.insert(0, node)
    return value, path                        # return optimal value with path

if __name__ == "__main__":
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

    leafs = {
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

    value, path = minimax_alpha_beta(tree, leafs, 'A')
    print("Optimal Solution : ",value)
    print(path)