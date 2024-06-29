import heapq as hq                                   #heap queue as hq

def path_cost(graph, path):
    cost = 0
    if len(path) < 2:
        return 0
    for i in range(0, len(path) - 1):                  #calculate overall path cost in graph
        cost += graph[path[i]][path[i+1]]
    return cost


def astar(graph, heuristic, start, goal):

    queue = [(heuristic[start], [start])]              #queue initialized with start node

    while len(queue) != 0:                             #checking whether the queue is empty or not

        cost, path = hq.heappop(queue)                 #pop of path with least path cost + heuristic cost
        key = path[-1]                                 #last node where the path left off

        if key == goal:                                #goal found
            return cost, path
        
        for i in graph[key]:                                        #visit all the nodes connected to path
            
            if i in path :                                          #avoiding deadlocks
                continue
            
            new_path = path + [i]                                   #new path
            new_cost = path_cost(graph, new_path) + heuristic[i]    #cost of the new path

            if new_path not in queue:
                hq.heappush(queue, (new_cost, new_path))           #push the new path with its cost

if __name__ == "__main__":

    Graph = {
        "A": {"B": 9, "C": 4, "D": 7},
        "B": {"E": 10},
        "C": {"E": 17, "F": 12},
        "D": {"F": 14},
        "E": {"G": 5},
        "F": {"G": 9}
    }

    Heuristic = {
        "A": 21,
        "B": 14,
        "C": 18,
        "D": 18,
        "E": 5,
        "F": 8,
        "G": 0,
    }

    cost, path = astar(Graph, Heuristic, "A", "G")
    print(path, cost)