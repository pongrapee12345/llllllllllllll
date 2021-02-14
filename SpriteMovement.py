import pygame  as game

WIDTH = 500
HEIGHT = 400
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)

class Player(game.sprite.Sprite):
    def __init__(self):
        game.sprite.Sprite.__init__(self)
        self.image = game.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.rect.y += 5
        if self.rect.top>HEIGHT:
            self.rect.bottom = 0
        
            
            



game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6002338 Game")
clock = game.time.Clock()

all_sprites = game.sprite.Group()
Character1 = Player()
all_sprites.add(Character1)

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