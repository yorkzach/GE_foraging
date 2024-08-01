# agent.py
import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carrying_food = False

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 10)

    def move_towards(self, target):
        target_x, target_y = target
        dx, dy = target_x - self.x, target_y - self.y
        dist = (dx**2 + dy**2) ** 0.5
        if dist > 0:
            dx, dy = dx / dist, dy / dist
            self.x += int(dx * 5)
            self.y += int(dy * 5)
