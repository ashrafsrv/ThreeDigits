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
                    self.build_path(self.expanded, node)
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
                    self.build_path(self.expanded, node)
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
            self.build_path(self.expanded, start)
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

    def get_min(self, fringe):
        if len(fringe) == 0:
            return None
        min_ = fringe[0]
        index = 0

        for i in range(len(fringe)):
            if min_.get_heuristic() > fringe[i].get_heuristic():
                min_ = fringe[i]

            if min_.get_heuristic() == fringe[i].get_heuristic():
                min_ = fringe[i]
                index = i

        return fringe.pop(index)

    def run_greedy(self, start, goal, forbidden):
        fringe = []
        start.set_heuristic(goal)
        fringe.append(start)

        found = False

        while not found:
            node = self.get_min(fringe)
            children = node.generate_children()

            if node not in self.expanded:

                self.expand(node)

                if self.count == 1000:
                    return self.expanded, []

                if node.get_value() == goal.get_value():
                    found = True
                    self.build_path(self.expanded, node)
                    return self.expanded, self.path

                for child in children:
                    child.set_parent(node)
                    child.set_heuristic(goal)
                    fringe.append(child)
                    fringe = sorted(fringe, key=self.cmp_to_key(self.my_cmp))

    def run_AStar(self, start, goal, forbidden):
            fringe = []
            start.set_heuristic(goal)
            start.set_eval()
            fringe.append(start)
            found = False

            while not found:
                node = self.get_min_2(fringe)
                children = node.generate_children()

                if node not in self.expanded:

                    self.expand(node)

                    if self.count == 1000:
                        return self.expanded, []

                    if node.get_value() == goal.get_value():
                        found = True
                        self.build_path(self.expanded, node)
                        return self.expanded, self.path

                    for child in children:
                        child.set_parent(node)
                        child.set_heuristic(goal)
                        child.set_eval()
                        fringe.append(child)
                        fringe = sorted(fringe, key=self.cmp_to_key(self.my_cmp_2))

    def get_min_2(self, fringe):
        if len(fringe) == 0:
            return None
        min_ = fringe[0]
        index = 0

        for i in range(len(fringe)):
            if min_.get_eval() > fringe[i].get_eval():
                min_ = fringe[i]

            if min_.get_eval() == fringe[i].get_eval():
                min_ = fringe[i]
                index = i

        return fringe.pop(index)

    def run_hill_climbing(self, start, goal, forbidden):
        start.set_heuristic(goal)
        current = start
        found = False

        while not found:
            current.generate_children()
            children = current.get_children()

            for child in children:
                child.set_parent(current)
                child.set_heuristic(goal)

            if current not in self.expanded:
                self.expand(current)

                if self.count == 1000:
                    return self.expanded, []

                if current.get_value() == goal.get_value():
                    found = True
                    self.build_path(self.expanded, current)
                    return self.expanded, self.path

            min_ = self.get_min(children)

            if min_ is None:
                return self.expanded, []

            if min_.get_heuristic() < current.get_heuristic():
                current = min_
            else:
                return self.expanded, []


    def my_cmp(self, node1, node2):
        if node1.get_heuristic() == node2.get_heuristic():
            return 0
        if node1.get_heuristic() < node2.get_heuristic():
            return -1
        if node1.get_heuristic() > node2.get_heuristic():
            return 1

    def my_cmp_2(self, node1, node2):
        if node1.get_eval() == node2.get_eval():
            return 0
        if node1.get_eval() < node2.get_eval():
            return -1
        if node1.get_eval() > node2.get_eval():
            return 1

    # Got the following function from code.activatestate.com
    def cmp_to_key(self, mycmp):
        'Convert a cmp= function into a key= function'
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
        return K

    @staticmethod
    def print_expanded(expanded):
        for i in range(len(expanded)):
            if i == len(expanded)-1:
                print("{} h({})".format(expanded[i], expanded[i].get_heuristic()))
            else:
                print("{} h({})".format(expanded[i], expanded[i].get_heuristic()), end=',')

    def build_path(self, llist, goal):
        self.path.append(goal)
        parent = goal.get_parent()

        while parent is not None:
            self.path.append(parent)
            parent = parent.get_parent()
        self.path.reverse()
