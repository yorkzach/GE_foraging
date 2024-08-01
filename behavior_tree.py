# behavior_tree.py
class Node:
    def tick(self):
        raise NotImplementedError

class CSequence(Node):
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children is not None else []

    def tick(self):
        for child in self.children:
            if not child.tick():
                return False
        return True

class Action(Node):
    def __init__(self, name, action_func):
        self.name = name
        self.action_func = action_func

    def tick(self):
        return self.action_func()

class Condition(Node):
    def __init__(self, name, condition_func):
        self.name = name
        self.condition_func = condition_func

    def tick(self):
        return self.condition_func()
