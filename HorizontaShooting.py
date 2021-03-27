import pygame  as game
import random

WIDTH = 500
HEIGHT = 650
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)
ORANGE =(252,95,6)
BLUE =(149, 227, 229)
WHITE =(255,255,255)

class Character(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.Surface((50,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.left = 20
        self.rect.bottom = HEIGHT-50
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
         bullet = Bullet(self.rect.centerx,self.rect.top)
         all_sprites.add(bullet)
         bulltes.add(bullet)



class Mob(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.Surface((30,40))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(HEIGHT-self.rect.width)            
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10:
            self.rect.x = random.randrange(HEIGHT-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

class Bullet(game.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = game.Surface((10,20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -10
        self.speedy =-10 

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <0 :
            self.kill

game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6002338 Game")
clock = game.time.Clock()



all_sprites = game.sprite.Group()
mobs = game.sprite.Group()
bulltes = game.sprite.Group()

character = Character()
all_sprites.add(character)

for i in range(10): 
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

running = True
while running:
    clock.tick(FPS)
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_SPACE:
                character.shoot()

        if event.type == game.KEYDOWN:
            if event.key == game.K_LEFT:
                character.speedx = -8
            if event.key == game.K_RIGHT:
                character.speedx = 8
        if event.type == game.KEYUP:
            if event.key == game.K_LEFT:
                character.speedx = 0
            if event.key == game.K_RIGHT:
                character.speedx = 0        
        



    all_sprites.update()
    
    hits = game.sprite.spritecollide(character,mobs,False)
    if hits:
        running = False

    hits = game.sprite.groupcollide(mobs,bulltes,True,True)
    for hit in hits:
        m =  Mob()
        all_sprites.add(m)
        mobs.add(m) 

    screen.fill(RED)
    all_sprites.draw(screen)
    game.display.flip()
game.quit()   