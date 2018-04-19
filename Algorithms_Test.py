from Algorithms import UISearch
from Node import Node

def print_expanded(expanded):
    for i in range(len(expanded)):
        if i == len(expanded)-1:
            print(expanded[i])
        else:
            print(expanded[i], end=',')

search = UISearch()
start = Node(3,2,0)
goal = Node(1,1,0)

forbidden = []
Node.set_forbidden(forbidden)
expanded, path = search.run_IDS(start, goal, forbidden)

print_expanded(expanded)

print_expanded(path)
