import pygame  as game
import os
WIDTH = 500
HEIGHT = 400
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)

class Player(game.sprite.Sprite):
    def __init__(self):
        game.sprite.Sprite.__init__(self)
        self.image = player_img
        #self.image = game.transform.flip(player_img,False,True)
        #self.image = game.Surface((50,50))
        #self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 5
        self.speedy = 5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left>WIDTH:
            self.rect.right = 0

        if self.rect.top < 100:
            self.speedy = 5
 
        elif self.rect.bottom > HEIGHT-100:
            self.speedy = -5
        elif self.rect.right > WIDTH:
             self.image = game.transform.flip(player_img,True,False)
             self.speedx = -5
        

        
            
            


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,'image')
img_file = os.path.join(img_folder,'chracter1.png')


game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6002338 Game")
player_img = game.image.load(os.path.join(img_folder,'character1.png')).convert()
#player_img = game.image.load(os.path.join(img_folder,'character1.png')).convert()
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