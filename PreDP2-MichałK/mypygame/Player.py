import pygame as py
from random import randint

CELL_SIZE = 60

class Snake:
    '''
    Snake that moves continuously and grows when eating coins
    '''
    def __init__(self, start_x, start_y, grid_r, grid_c):
       
        self.body = [(start_x, start_y)]
        self.direction = (1, 0)  
        self.next_direction = (1, 0)  
        self.grid_r = grid_r
        self.grid_c = grid_c
        self.coins = 0
        self.alive = True
        self.grow_pending = False
    
    def set_direction(self, event):
        '''Handle input from arrow keys and WASD'''
        keys = py.key.get_pressed()
        
        
        if keys[py.K_LEFT] and self.direction != (1, 0):
            self.next_direction = (-1, 0)
        if keys[py.K_RIGHT] and self.direction != (-1, 0):
            self.next_direction = (1, 0)
        if keys[py.K_UP] and self.direction != (0, 1):
            self.next_direction = (0, -1)
        if keys[py.K_DOWN] and self.direction != (0, -1):
            self.next_direction = (0, 1)
        
        if keys[py.K_a] and self.direction != (1, 0):
            self.next_direction = (-1, 0)
        if keys[py.K_d] and self.direction != (-1, 0):
            self.next_direction = (1, 0)
        if keys[py.K_w] and self.direction != (0, 1):
            self.next_direction = (0, -1)
        if keys[py.K_s] and self.direction != (0, -1):
            self.next_direction = (0, 1)
    
    def move(self):
        '''Move snake forward, grow if pending, check collisions'''
        self.direction = self.next_direction
        
        
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_x = (head_x + dx * CELL_SIZE) % (self.grid_c * CELL_SIZE)
        new_y = (head_y + dy * CELL_SIZE) % (self.grid_r * CELL_SIZE)
        
        new_head = (new_x, new_y)
        
        
        if new_head in self.body:
            self.alive = False
            return
        
       
        self.body.insert(0, new_head)
        
        
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def eat_coin(self):
        '''Called when snake eats a coin'''
        self.coins += 1
        self.grow_pending = True
    
    def draw(self, screen):
        '''Draw snake body'''
        
        head_x, head_y = self.body[0]
        py.draw.rect(screen, (0, 255, 0), (head_x, head_y, CELL_SIZE, CELL_SIZE))
        
       
        for i in range(1, len(self.body)):
            seg_x, seg_y = self.body[i]
            py.draw.rect(screen, (0, 200, 0), (seg_x, seg_y, CELL_SIZE, CELL_SIZE))
            py.draw.rect(screen, (0, 150, 0), (seg_x, seg_y, CELL_SIZE, CELL_SIZE), 2)

class Coin:
    '''Represents a coin to collect'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        py.draw.circle(screen, (255, 215, 0), (self.x + CELL_SIZE//2, self.y + CELL_SIZE//2), CELL_SIZE//4)