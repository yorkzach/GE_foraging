# GEmain.py
import state
from genetic_algorithm import GeneticAlgorithm

def main():
    # Initialize the genetic algorithm
    ga = GeneticAlgorithm(population_size=50, generations=100, mutation_rate=0.1)

    # Evolve the best behavior tree
    best_tree = ga.evolve()

    # Integrate the best behavior tree into the agent's logic
    agent_behavior_tree = eval(best_tree)  # This assumes the tree is in a string format that can be eval'd

    # Run the main loop with the evolved behavior tree
    while True:
        agent_behavior_tree.tick()
        # Rest of your main loop

if __name__ == "__main__":
    main()
