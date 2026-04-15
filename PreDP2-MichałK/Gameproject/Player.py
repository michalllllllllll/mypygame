from dataclasses import dataclass
import pygame as py

class Player:
    '''
    Create a player with x, y coordinates
    and w, h as it's width and height
    '''
    #static variable/ class variables
    speedX , speedY = 5, 5
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = py.Rect(self.x, self.y, 60, 60)
        self.coins = 0
    
    def draw(self, screen):
        py.draw.rect(screen, (0, 255, 0), self.rect)
    
    def move(self, screen, grid):
        keys = py.key.get_pressed()
        r = self.y // 60  # row
        c = self.x // 60  # col
        if keys[py.K_LEFT] and c - 1 >= 0 and grid[r][c-1] != 0:
            self.x -= 60
        if keys[py.K_RIGHT] and c + 1 < 9 and grid[r][c+1] != 0:
            self.x += 60
        if keys[py.K_UP] and r - 1 >= 0 and grid[r-1][c] != 0:
            self.y -= 60
        if keys[py.K_DOWN] and r + 1 < 9 and grid[r+1][c] != 0:
            self.y += 60
        self.rect = py.Rect(self.x, self.y, 60, 60)
    
    def collision(self, obstacle):
        if abs(self.x - obstacle.x) < self.w:
            if abs(self.y - obstacle.y) <self.h:
                if(not Player.collide) - True:
                    print("COLLISION")
                    Player.collide = True
            else:
                Player.collide = False
        else:
            Player.collide = False

@dataclass
class Obstacle:
    x: int
    y: int

    def draw(self, screen):
        py.draw.rect(screen, (100, 100, 100), (self.x, self.y, 60, 60))