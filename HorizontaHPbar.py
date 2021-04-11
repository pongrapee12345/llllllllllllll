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
snd_dir = path.join(path.dirname(__file__),'snd')



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
        self.hp = 100

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
         shoot_sound.play()



class Mob(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ##self.image = game.transform.scale(enemy_img,(50,40))
        self.image_orig = random.choice(enemy_imgs)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/2)
        #game.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.x = random.randrange(HEIGHT-self.rect.width)            
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.lastupdate = game.time.get_ticks()
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10:
            self.rect.x = random.randrange(HEIGHT-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)
    def rotate(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 50:
            self.lastupdate = now
            self.rot = (self.rot + self.rot_speed)%360
            new_image = game.transform.rotate(self.image_orig , self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center     

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
#Imags and sound
background = game.image.load(path.join(img_dir , 'background.png')).convert()
background_rect = background.get_rect()

shoot_sound = game.mixer.Sound(path.join(snd_dir,'shoot.mp3'))
game.mixer.music.load(path.join(snd_dir, 'background.mp3'))
game.mixer.music.set_volume(0.5)

player_img = game.image.load(path.join(img_dir , "player.png")).convert()

#enemy_img = game.image.load(path.join(img_dir, 'enemy.png')).convert()
enemy_imgs =[]
enemy_list =['enemy.png','enemy2.png','enemy3.png']
for img in enemy_list:
    enemy_imgs.append(game.image.load(path.join(img_dir, img)).convert())  



bullet_img = game.image.load(path.join(img_dir , 'fire.png')).convert()

all_sprites = game.sprite.Group()
mobs = game.sprite.Group()
bulltes = game.sprite.Group()

character = Character()
all_sprites.add(character)

def NewMob():
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)


for i in range(5): 
    NewMob()


score = 0 

font_name = game.font.match_font('arial')
def draw_text(surf , text , size , x , y):
    font = game.font.Font(font_name , size)
    text_surface = font.render(text , True , RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface , text_rect)

def draw_hp_bar(surf , x ,y , hp):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 140
    BAR_HIGHT = 50
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = game.Rect(x , y , BAR_LENGTH , BAR_HIGHT)
    fill_rect = game.Rect(x , y , fill , BAR_HIGHT)
    game.draw.rect(surf , RED , fill_rect)
    if character.hp < 50:
        game.draw.rect(surf , WHITE , fill_rect)
    game.draw.rect(surf , WHITE , outline_rect , 2)

game.mixer.music.play(loops=-1)

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
    
    hits = game.sprite.spritecollide(character,mobs,True,game.sprite.collide_circle)
    if hits:
        for hit in hits:
            character.hp -= 10
            NewMob()
        if character.hp <=10:
            running = False

    hits = game.sprite.groupcollide(mobs,bulltes,True,True)
    for hit in hits:
        score += 50
        NewMob()
#Render
    screen.fill(RED)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen , str(score) , 50 , WIDTH / 2 , 10)
    draw_hp_bar(screen,5,5,character.hp)
    game.display.flip()
game.quit()   