import heapq as hq                                   #heap queue as hq

Graph = {                                            #graph
    "B": {"C": 7, "N": 8},
    "C": {"M": 3, "N": 2},
    "M": {"B": 4, "S": 1},
    "N": {"M": 3, "S": 5},
    "S": {},
}

Heuristic = {                                         #heuristic function
    "B": 2,
    "C": 3,
    "M": 5,
    "N": 4,
    "S": 3,
}

def path_cost(graph, path):
    cost = 0
    if len(path) < 2:
        return 0
    for i in range(0, len(path) - 1):                  #calculate overall path cost in graph
        cost += graph[path[i]][path[i+1]]
    return cost


def astar(graph, heuristic, start, goal):

    opened = [(heuristic[start], [start])]              #priority queue initialized with start node
    closed = []

    while len(opened) != 0:                             #checking whether the queue is empty or not

        hq.heapify(opened)                              #heapifying queue

        print("Opened list : ")
        print(opened)
        print("Closed list : ")
        print(closed)

        cost, path = hq.heappop(opened)                 #pop of path with least path cost + heuristic cost
        key = path[-1]                                  #last node where the path left off

        if key == goal:                                 #goal found
            print("Optimal Solution is found : ", path," = ", cost)   
            break
        else:
            closed.append((cost, path))

        for i in graph[key]:                                        #visit all the nodes connected to path
            if i in path :                                          #avoiding deadlocks
                continue
            new_path = path + [i]                                   #new path
            new_cost = path_cost(graph, new_path) + heuristic[i]    #calculate cost of the new path

            if new_path not in opened and closed:
                opened.append((new_cost, new_path))                 #push the new path with its cost

    else:                                                           #no solution found
        print("Opened list : ")
        print(opened)
        print("Closed list : ")
        print(closed)
        print("\nNo Solution")                                     

astar(Graph, Heuristic, "B", "S")
