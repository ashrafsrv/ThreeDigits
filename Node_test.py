from Node import Node

def print_expanded(expanded):
    for i in range(len(expanded)):
        if i == len(expanded)-1:
            print(expanded[i])
        else:
            print(expanded[i], end=',')

node = Node(1,0,0)
node.set_parent(Node(0,0,0))
node.generate_children()
print_expanded(node.get_children())
