import pygame  as game
import random
from os import path

WIDTH = 500
HEIGHT = 650
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)
ORANGE =(252,95,6)
BLUE =(149, 227, 229)
WHITE =(255,255,255)

img_dir = path.join(path.dirname(__file__), 'img')



class Character(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.transform.scale(player_img, (50,40))
        self.rect = self.image.get_rect()
        self.radius = 25
        #game.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.image.set_colorkey(BLACK)
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
        self.image = game.transform.scale(enemy_img,(50,40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/2)
        #game.draw.circle(self.image,RED,self.rect.center,self.radius)
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
        self.image = game.transform.scale(bullet_img,(10 ,10))
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

background = game.image.load(path.join(img_dir , 'background.png')).convert()
background_rect = background.get_rect()

player_img = game.image.load(path.join(img_dir , "player.png")).convert()

enemy_img = game.image.load(path.join(img_dir, 'enemy.png')).convert()

bullet_img = game.image.load(path.join(img_dir , 'fire.png')).convert()

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
    
    hits = game.sprite.spritecollide(character,mobs,False,game.sprite.collide_circle)
    if hits:
        running = False

    hits = game.sprite.groupcollide(mobs,bulltes,True,True)
    for hit in hits:
        m =  Mob()
        all_sprites.add(m)
        mobs.add(m) 

    screen.fill(RED)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    game.display.flip()
game.quit()   