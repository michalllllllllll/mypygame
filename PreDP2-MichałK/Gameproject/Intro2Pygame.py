import pygame as py
py.init()
width, height = 600, 600


screen = py.display.set_mode((width, height))
py.display.set_caption("Intro to pygame")

screen.fill("#eb0c7f")
run = True
while run:
    for event in py.event.get():
            if event.type == py.QUIT:
                  run = False

    py.draw.line(screen, "#9fce07", (0,0), (width/2, height/2))
    py.draw.line(screen, "#7e31e3", (600,0), (width/2, height/2))
    py.draw.line(screen, "#54d184", (0,600), (width/2, height/2))
    py.draw.line(screen, "#412121", (600,600), (width/2, height/2))
    py.draw.rect(screen, "#956700", (250,250,100,100))
    #canvas color rectangle(x-pos, y-pos, width, height)
    py.draw.circle(screen, "#36165E", (300,500), 75)
    #canvas color (x-pos, y-pos), radius
    py.draw.ellipse(screen, "#009595", (150,250,50,100))
    #canvas color (x-pos of top left, y-pos of top left, width, length)
    py.draw.ellipse(screen, "#009595", (150,50,300,100))
    py.draw.ellipse(screen, "#009595", (400,250,50,100))
    py.draw.circle(screen, "#36165E", (275,300), 25)
    py.draw.circle(screen, "#36165E", (325,300), 25)
    py.display.flip()
py.quit()
