# state.py (adapted for py_trees with memory)
import py_trees
import conditions_actions as ca

def build_behavior_tree():
    # Root of the tree
    root = py_trees.composites.Selector(name="Root", memory=True)

    # Define find and return food state
    find_and_return_food = py_trees.composites.Sequence(name="Find and Return Food", memory=True)
    find_and_return_food.add_children([
        ca.FoodAvailable(),
        ca.GoToPatch(),
        ca.PickUp(),
        ca.ReturnToDen(),
        ca.DropOff()
    ])

    # Define explore and eat state
    explore_and_eat = py_trees.composites.Sequence(name="Explore and Eat", memory=True)
    explore_and_eat.add_children([
        ca.Hungry(),
        ca.SafeArea(),
        ca.Explore(),
        ca.Consume()
    ])

    # Add states to the root
    root.add_children([find_and_return_food, explore_and_eat])

    return root
