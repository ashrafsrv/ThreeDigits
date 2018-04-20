from Algorithms import UISearch
from Node import Node

def print_expanded(expanded):
    for i in range(len(expanded)):
        if i == len(expanded)-1:
            print(expanded[i])
        else:
            print(expanded[i], end=',')

search = UISearch()
start = Node(0,0,0)
goal = Node(0,0,1)



forbidden = []
Node.set_forbidden(forbidden)
expanded, path = search.run_hill_climbing(start, goal, forbidden)

print_expanded(expanded)


print_expanded(path)
