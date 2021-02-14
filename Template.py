import pygame  as game

WIDTH = 500
HEIGHT = 400
FPS =30

RED = (255,0,0)
BLACK =(0,0,0)
game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6002338 Game")
clock = game.time.Clock()

all_sprites = game.sprite.Group()

running = True
while running:
    clock.tick(FPS)
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
    all_sprites.update()    
    screen.fill(RED)
    all_sprites.draw(screen)
    game.display.flip()
game.quit()   