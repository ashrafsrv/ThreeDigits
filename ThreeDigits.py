import sys
import os
from Algorithms import UISearch
from Node import Node

def make_node(string):
    num = list(string)
    left = int(num[0])
    middle = int(num[1])
    right = int(num[2])

    node = Node(left, middle, right)
    return node

def print_list(llist):
    for i in range(len(llist)):
        if i == len(llist)-1:
            print(llist[i])
        else:
            print(llist[i], end=',')

if len(sys.argv) != 3:
    sys.stderr.write("Incorrect number of arguments.\n")
    sys.exit(1)

algorithm = sys.argv[1]
filename = sys.argv[2]

content = []

with open(filename, 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

if len(content) == 3:
    start = content[0]
    goal = content[1]
    forbidden_line = content[2]
elif len(content) == 2:
    start = content[0]
    goal = content[1]
    forbidden_line = ""


start_node = make_node(start)
goal_node = make_node(goal)

forbidden = []
forbidden_list = forbidden_line.split(',')

if forbidden_line != "":
    for state in forbidden_list:
        forbidden.append(make_node(state))



search = UISearch()
Node.set_forbidden(forbidden)
expanded = []
path = []

if algorithm == "B":
    expanded, path = search.run_BFS(start_node, goal_node, forbidden)
if algorithm == "D":
    expanded, path = search.run_DFS(start_node, goal_node, forbidden)
if algorithm == "I":
    expanded, path = search.run_IDS(start_node, goal_node, forbidden)

if len(path) == 0:
    print("No solution found.")
    print_list(expanded)
else:
    print_list(path)
    print_list(expanded)
