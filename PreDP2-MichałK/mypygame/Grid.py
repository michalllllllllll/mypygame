from random import randint
import pygame as py
from Player import Snake, Coin


grid_r, grid_c = 9, 9
cell_size = 60


width, height = cell_size * grid_c, cell_size * grid_r
panel = 150


py.init()
screen = py.display.set_mode((width + panel, height))
py.display.set_caption("Snake Game")
clock = py.time.Clock()
font = py.font.SysFont(None, 30)
FPS = 60


bgImg = py.Surface((width, height))
bgImg.fill((255, 255, 255))


snake = Snake(0, 0, grid_r, grid_c)

coins = []
def spawn_coin():
    #Spawn a random coin on the board
    while True:
        x = randint(0, grid_c - 1) * cell_size
        y = randint(0, grid_r - 1) * cell_size
        
        if (x, y) not in snake.body:
            coins.append(Coin(x, y))
            break


for _ in range(3):
    spawn_coin()


move_counter = 0
move_frequency = 8  

run = True
game_over = False

while run:
    clock.tick(FPS)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    
    snake.set_direction(None)
    
    move_counter += 1
    if move_counter >= move_frequency:
        move_counter = 0
        snake.move()
        
        if not snake.alive:
            game_over = True
    
    
    snake_head = snake.body[0]
    for coin in coins[:]:
        if (coin.x, coin.y) == snake_head:
            snake.eat_coin()
            coins.remove(coin)
            spawn_coin()
    
    screen.blit(bgImg, (0, 0))
 
    for i in range(grid_r + 1):
        py.draw.line(screen, (200, 200, 200), (0, i * cell_size), (width, i * cell_size))
    for i in range(grid_c + 1):
        py.draw.line(screen, (200, 200, 200), (i * cell_size, 0), (i * cell_size, height))

    for coin in coins:
        coin.draw(screen)
    
 
    snake.draw(screen)
    
   
    py.draw.rect(screen, "#26195A", (width, 0, panel, height))
    
  
    text_y = 20
    info_texts = [
        f"Coins: {snake.coins}",
        f"Length: {len(snake.body)}",
        f"Direction: {snake.direction}",
    ]
    
    if game_over:
        info_texts.append("GAME OVER!")
    
    for text in info_texts:
        textSurface = font.render(text, True, "#ffffff")
        screen.blit(textSurface, (width + 10, text_y))
        text_y += 40
    
    py.display.flip()

py.quit()

