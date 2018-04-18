from queue import Queue
from stack import Stack
from Node import Node

class UISearch:

    def __init__(self):
        self.expanded = []
        self.path = []
        self.count = 0
        self.recurstack = []


    def expand(self,node):
        node.generate_children()
        self.expanded.append(node)
        self.count += 1


    def run_BFS(self, start, goal, forbidden):
        fringe = Queue()
        fringe.put(start)

        while not fringe.empty():
            node = fringe.get()

            if node not in self.expanded:

                self.expand(node)

                if self.count == 1000:
                    return self.expanded, []

                if node.get_left() == goal.get_left() and node.get_middle() == goal.get_middle() and node.get_right() == goal.get_right():
                    self.set_path(self.expanded, node)
                    return self.expanded, self.path

                for child in node.get_children():
                    fringe.put(child)
                    child.set_parent(node)
        return self.expanded, []

    def run_DFS(self, start, goal, forbidden):
        fringe = Stack()
        fringe.push(start)

        while not fringe.isEmpty():
            node = fringe.pop()
            node.generate_children()
            if node not in self.expanded:

                self.expand(node)

                if self.count == 10:
                    return self.expanded, []

                if node.get_left() == goal.get_left() and node.get_middle() == goal.get_middle() and node.get_right() == goal.get_right():
                    self.set_path(self.expanded, node)
                    return self.expanded, self.path

                children = node.get_children()
                children_copy = children[:]
                children_copy.reverse()

                for child in children_copy:
                    fringe.push(child)
                    child.set_parent(node)

        return self.expanded, []

    def set_path(self, llist, goal):
        self.path.append(goal)
        parent = goal.get_parent()

        while parent is not None:
            self.path.append(parent)
            parent = parent.get_parent()
        self.path.reverse()
