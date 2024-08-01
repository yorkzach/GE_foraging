# main.py
import pygame
import random
import py_trees
from agent import Agent
import conditions_actions as ca
import state

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Agent World")
clock = pygame.time.Clock()

# Dens and food locations
dens = [(100, 100), (700, 500)]
food_locations = [(400, 300), (200, 400), (600, 200), (500, 100)]

def regenerate_food():
    if len(food_locations) < 5:
        new_food = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
        food_locations.append(new_food)

def main():
    agent = Agent(400, 300)
    ca.set_world_state(agent, food_locations, dens)
    
    # Build behavior tree
    bt = state.build_behavior_tree()
    tree = py_trees.trees.BehaviourTree(root=bt)

    running = True
    step_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Draw dens
        for den in dens:
            pygame.draw.circle(screen, GREEN, den, 20)

        # Draw food locations
        for food in food_locations:
            pygame.draw.circle(screen, RED, food, 10)

        # Update and draw agent
        agent.draw(screen)
        tree.tick()

        pygame.display.flip()
        clock.tick(FPS)

        step_count += 1
        if step_count % 100 == 0:
            # Use py_trees built-in method to visualize the tree
            try:
                py_trees.display.render_dot_tree(bt, name="behavior_tree")
            except FileNotFoundError:
                print("Graphviz 'dot' executable not found. Install Graphviz and ensure 'dot' is in your PATH.")
        
        if step_count % 50 == 0:
            regenerate_food()
    
    pygame.quit()

if __name__ == "__main__":
    main()
