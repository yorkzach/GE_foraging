# conditions_actions.py (updated for py_trees)
import random
import py_trees

agent = None
food_locations = None
dens = None

def set_world_state(agent_ref, food_locs, dens_locs):
    global agent, food_locations, dens
    agent = agent_ref
    food_locations = food_locs
    dens = dens_locs

class FoodAvailable(py_trees.behaviour.Behaviour):
    def __init__(self, name="Food Available"):
        super(FoodAvailable, self).__init__(name)

    def update(self):
        if any(food for food in food_locations):
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class AtDen(py_trees.behaviour.Behaviour):
    def __init__(self, name="At Den"):
        super(AtDen, self).__init__(name)

    def update(self):
        if any((den[0] - agent.x) ** 2 + (den[1] - agent.y) ** 2 < 400 for den in dens):
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class Hungry(py_trees.behaviour.Behaviour):
    def __init__(self, name="Hungry"):
        super(Hungry, self).__init__(name)

    def update(self):
        if not agent.carrying_food:
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class SafeArea(py_trees.behaviour.Behaviour):
    def __init__(self, name="Safe Area"):
        super(SafeArea, self).__init__(name)

    def update(self):
        return py_trees.common.Status.SUCCESS  # Placeholder for actual logic

class PickUp(py_trees.behaviour.Behaviour):
    def __init__(self, name="Pick Up"):
        super(PickUp, self).__init__(name)

    def update(self):
        for food in food_locations:
            if (food[0] - agent.x) ** 2 + (food[1] - agent.y) ** 2 < 100:
                agent.carrying_food = True
                food_locations.remove(food)
                return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class DropOff(py_trees.behaviour.Behaviour):
    def __init__(self, name="Drop Off"):
        super(DropOff, self).__init__(name)

    def update(self):
        if agent.carrying_food and any((den[0] - agent.x) ** 2 + (den[1] - agent.y) ** 2 < 400 for den in dens):
            agent.carrying_food = False
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class Consume(py_trees.behaviour.Behaviour):
    def __init__(self, name="Consume"):
        super(Consume, self).__init__(name)

    def update(self):
        if agent.carrying_food:
            agent.carrying_food = False
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class Explore(py_trees.behaviour.Behaviour):
    def __init__(self, name="Explore"):
        super(Explore, self).__init__(name)

    def update(self):
        agent.x += random.randint(-5, 5)
        agent.y += random.randint(-5, 5)
        agent.x = max(0, min(800, agent.x))
        agent.y = max(0, min(600, agent.y))
        return py_trees.common.Status.SUCCESS

class GoToPatch(py_trees.behaviour.Behaviour):
    def __init__(self, name="Go To Patch"):
        super(GoToPatch, self).__init__(name)

    def update(self):
        if food_locations:
            agent.move_towards(food_locations[0])
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class ReturnToDen(py_trees.behaviour.Behaviour):
    def __init__(self, name="Return To Den"):
        super(ReturnToDen, self).__init__(name)

    def update(self):
        if dens:
            agent.move_towards(dens[0])
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE
