# grammar.py
grammar = {
    "BT": ["Selector(memory=True, children=[<Seq>])"],
    "Seq": ["Sequence(memory=True, children=[<CondActionList>])"],
    "CondActionList": ["<CondAction>", "<CondAction>, <CondActionList>"],
    "CondAction": ["<Condition>", "<Action>"],
    "Condition": ["FoodAvailable()", "AtDen()", "Hungry()", "SafeArea()"],
    "Action": ["PickUp()", "DropOff()", "Consume()", "Explore()", "GoToPatch()", "ReturnToDen()"]
}
