from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        pass

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
background = transform.scale(image.load(''), (win_width, win_height))

font.init()
font_1 = font.Font(None, 30)

run = True
finish = False 
clock = time.Clock()
FPS = 60
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0,0))
        # hero.reset()
        # hero.update()
        
    display.update()
    clock.tick(FPS)