import random

from Snake import screen_width, screen_height, green
import pygame as pg


class Frog:
    # Initialization
    def __init__(self):
        self.x = screen_width/2
        self.y = screen_height/4
        self.color = green
        self.width = 10
        self.height = 10
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 5

    # Displays the frog on screen
    def draw_frog(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snake eat the frog?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the frog when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
