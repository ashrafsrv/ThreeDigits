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
        # start.generate_children()

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

    def set_path(self, llist, goal):
        self.path.append(goal)
        parent = goal.get_parent()

        while parent is not None:
            self.path.append(parent)
            parent = parent.get_parent()
        self.path.reverse()
