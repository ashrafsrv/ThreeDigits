from queue import Queue
from stack import Stack
from Node import Node

class UISearch:

    def __init__(self):
        self.expanded = []
        self.path = []
        self.count = 0

    def expand(self,node):
        node.generate_children()
        self.expanded.append(node)
        self.count += 1


    def run_BFS(self, start, goal, forbidden):
        fringe = Queue()
        fringe.put(start)
        i = 0
        while not fringe.empty():
            node = fringe.get()

            if node not in self.expanded:
                self.expand(node)

                if self.count == 1000:
                    return self.expanded, []

                if node.get_value() == goal.get_value():
                    self.set_path(self.expanded, node)
                    return self.expanded, self.path

                for child in node.get_children():
                    fringe.put(child)
                    child.set_parent(node)
                    child.generate_children()
        return self.expanded, []

    def run_DFS(self, start, goal, forbidden):
        fringe = Stack()
        fringe.push(start)

        while not fringe.isEmpty():
            node = fringe.pop()


            if node not in self.expanded:

                self.expand(node)

                if self.count == 1000:
                    return self.expanded, []

                if node.get_value() == goal.get_value():
                    self.set_path(self.expanded, node)
                    return self.expanded, self.path

                children = node.get_children()
                children_copy = children[:]
                children_copy.reverse()

                for child in children_copy:
                    fringe.push(child)
                    child.set_parent(node)
                    child.generate_children()

        return self.expanded, []

    def run_IDS(self, start, goal, forbidden):

        depth = 0
        global_expanded = []

        while(self.count < 1000):
            temp, path, boolean = self.run_DLS(start, goal, forbidden, depth)
            global_expanded.extend(temp)

            if len(global_expanded) >= 1000:
                return global_expanded[:999], []
                
            if boolean == True:
                return global_expanded, self.path
            depth += 1
            self.expanded = []
        return global_expanded, []

    def run_DLS(self, start, goal, forbidden, depth):
        start.generate_children()
        if start not in self.expanded:
            self.expand(start)

        if start.get_value() == goal.get_value():
            self.set_path(self.expanded, start)
            return self.expanded, self.path, True

        if depth == 0:
            return self.expanded, [], False

        children = start.get_children()

        for child in children:
            child.set_parent(start)
            e, p, boo = self.run_DLS(child, goal, forbidden, depth-1)
            if boo:
                return self.expanded, self.path, True

        return self.expanded, [], False


    def print_expanded(self, expanded):
        for i in range(len(expanded)):
            if i == len(expanded)-1:
                print(expanded[i])
            else:
                print(expanded[i], end=',')

    def set_path(self, llist, goal):
        self.path.append(goal)
        parent = goal.get_parent()

        while parent is not None:
            self.path.append(parent)
            parent = parent.get_parent()
        self.path.reverse()
