class Node:
    forbidden = []
    def __init__(self, left, middle, right):
        self.left = left
        self.middle = middle
        self.right = right
        self.children = []
        self.parent = None
        self.value = int(self.__str__())
        self.heuristic = 0
        self.pathcost = 0
        self.eval = 0

    def get_value(self):
        return self.value

    @classmethod
    def set_forbidden(cls, forbidden):
        cls.forbidden = forbidden

    def set_heuristic(self, goal):
        self.heuristic = abs(self.get_left()-goal.get_left()) + abs(self.get_middle() - goal.get_middle()) + abs(self.get_right() - goal.get_right())

    def get_heuristic(self):
        return self.heuristic

    def set_pathcost(self, cost):
        self.pathcost = cost

    def get_pathcost(self):
        return self.pathcost

    def set_eval(self):
        path = []
        path.append(self)
        parent = self.get_parent()
        pathcost = 0

        while parent is not None:
            path.append(parent)
            parent = parent.get_parent()
            pathcost += 1

        heuristic = self.get_heuristic()
        val = heuristic + pathcost
        self.eval = val

    def get_eval(self):
        return self.eval

    def get_forbidden(cls):
        return cls.forbidden

    def set_parent(self, parent):
        if parent is not None:
            self.parent = parent

    def set_children(self, valid_children):
        self.children = valid_children

    def get_children(self):
        return self.children

    def get_left(self):
        return self.left

    def get_middle(self):
        return self.middle

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def remove_children(self):
        self.children = []

    def generate_possible_children(self):
        children = []
        if self.left != 0:
            children.append(Node(self.left - 1, self.middle, self.right))
        if self.left != 9:
            children.append(Node(self.left + 1, self.middle, self.right))
        if self.middle != 0:
            children.append(Node(self.left, self.middle - 1, self.right))
        if self.middle != 9:
            children.append(Node(self.left, self.middle + 1, self.right))
        if self.right != 0:
            children.append(Node(self.left, self.middle, self.right - 1))
        if self.right != 9:
            children.append(Node(self.left, self.middle, self.right + 1))
        self.children = children
        return children

    def generate_children(self):
        children = self.generate_possible_children()
        new_children = []
        found_forbidden = False

        for child in children:

            parent = self.get_parent()

            if parent is not None:

                if parent.get_left() != self.get_left():
                    if child.get_left() != self.get_left():
                        continue
                if parent.get_middle() != self.get_middle():
                    if child.get_middle() != self.get_middle():
                        continue
                if parent.get_right() != self.get_right():
                    if child.get_right() != self.get_right():
                        continue

                for node in self.forbidden:
                    if child.get_value() == node.get_value():
                        found_forbidden = True

                if found_forbidden == True:
                    found_forbidden = False
                    continue

            new_children.append(child)

        self.set_children(new_children)
        return self.children

    def __eq__(self, other):
        listA = self.get_children()
        listB = other.get_children()

        if self.left == other.get_left() and self.middle == other.get_middle() and self.right == other.get_right():
            if len(listA) != len(listB):
                return False

            for i in range(len(listA)):
                if listA[i].get_value() != listB[i].get_value():
                    return False
            return True
        return False

    def __ne__(self, other):
        return not self == other

    # def __lt__(self, other):
    #     return self.heuristic < other.get_heuristic()
    #
    # def __gt__(self, other):
    #     return self.heuristic > other.get_heuristic()

    def __hash__(self):
        return hash((self.left, self.middle, self.right))

    def __str__(self):
        return str(self.left) + str(self.middle) + str(self.right)
