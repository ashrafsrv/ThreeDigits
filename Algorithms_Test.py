from Algorithms import UISearch
from Node import Node

def print_expanded(expanded):
    for i in range(len(expanded)):
        if i == len(expanded)-1:
            print(expanded[i])
        else:
            print(expanded[i], end=',')

search = UISearch()
start = Node(3,4,5)
goal = Node(5,5,5)

forbidden = [Node(4,5,5), Node(5,4,5), Node(5,5,4)]
Node.set_forbidden(forbidden)
expanded, path = search.run_BFS(start, goal, forbidden)

print_expanded(expanded)

print_expanded(path)
