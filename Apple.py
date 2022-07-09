import random

from Snake import screen_width, screen_height, red
import pygame as pg


class Apple:
    # Initialization
    def __init__(self):
        self.x = screen_width/2
        self.y = screen_height/4
        self.color = red
        self.width = 10
        self.height = 10
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 1

    # Displays the apple on screen
    def draw_apple(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snake eat the apple?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the apple when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
