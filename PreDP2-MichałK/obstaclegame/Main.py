import pygame
from random import randint
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

size = 50

#edit

grid = [[randint(0,1) for i in range(10)] for j in range(10)]
grid[5][5] = 1  # Ensure player starts on empty space


class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (self.x, self.y, self.w, self.h)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


obstacles = []
for row in range(10):
    for col in range(10):
        if grid[row][col] == 0:
            obstacles.append(Obstacle(col*size, row*size))


player = Player(5*size, 5*size, size, size)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_x = player.x - size
                if new_x < 0:
                    print("You Win!")
                    running = False
                else:
                    row = int(player.y / size)
                    col = int(new_x / size)
                    if grid[row][col] == 1:
                        player.x = new_x
                        player.rect = (player.x, player.y, player.w, player.h)
            elif event.key == pygame.K_RIGHT:
                new_x = player.x + size
                if new_x > 450:
                    print("You Win!")
                    running = False
                else:
                    row = int(player.y / size)
                    col = int(new_x / size)
                    if grid[row][col] == 1:
                        player.x = new_x
                        player.rect = (player.x, player.y, player.w, player.h)
            elif event.key == pygame.K_UP and player.y > 0:
                new_y = player.y - size
                row = int(new_y / size)
                col = int(player.x / size)
                if grid[row][col] == 1:
                    player.y = new_y
                    player.rect = (player.x, player.y, player.w, player.h)
            elif event.key == pygame.K_DOWN and player.y < 450:
                new_y = player.y + size
                row = int(new_y / size)
                col = int(player.x / size)
                if grid[row][col] == 1:
                    player.y = new_y
                    player.rect = (player.x, player.y, player.w, player.h)


    player.draw()
    for obs in obstacles:
        obs.draw()
    
    # Draw grid lines
    for i in range(11):
        pygame.draw.line(screen, (255, 255, 255), (0, i * size), (500, i * size))
        pygame.draw.line(screen, (255, 255, 255), (i * size, 0), (i * size, 500))
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()

