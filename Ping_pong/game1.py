from pygame import *
from random import randint
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):

   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, w = 65, h = 65):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed_x = player_speed
        self.speed_y = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def run(self):
        self.rect.x -= self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= 700:
            self.speed_y *= -1        


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_y

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_y 

def sprites_load(folder:str, file_name:str, size:tuple, colorkey:tuple = None):    
    sprites = []
    load = True
    num = 1
    while load:
        try:
            spr = transform.scale(image.load(f'{folder}\\{file_name}{num}.png'),size)
            if colorkey: spr.set_colorkey((0,0,0))
            sprites.append(spr)
            num += 1
        except:
            load = False
    return sprites

    

def win():
    if ball.rect.x <= 0:

        window.blit(player2_win,(0,0))
    elif ball.rect.x >= 700:

        window.blit(player1_win,(0,0))


def diff_p1():
    if ball.rect.x == player1.rect.x and ball.rect.y == player1.rect.y:
        ball_speed *= -1


def diff_p2():
    if ball.rect.x == player2.rect.x and ball.rect.y == player2.rect.y:
        ball_speed *= -1

font.init()
font1 = font.Font(None, 36)
ball_speed = 5


#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
#display.set_caption("Galaxy")

background = transform.scale(image.load("pictures/blueback2.png"), (win_width, win_height))
player1_win = transform.scale(image.load("pictures/player1_win.png"), (win_width, win_height))
player2_win = transform.scale(image.load("pictures/player2_win.png"), (win_width, win_height))

#Персонажи игры:
player1 = Player("pictures/ping_rocket1.png", 50, 100, 15, 20, 70)
player2 = Player("pictures/ping_rocket2.png", 650, 15, 15, 20, 70)
ball = GameSprite("pictures/Tennis-Ball-Download-Free-PNG.png", 450, 250, ball_speed, 50, 50)

 
game = True

clock = time.Clock()
FPS = 60

finish = False

col_num = 0
while game:


    for e in event.get():
        if e.type == QUIT:
            game = False
    

    if not finish:
        window.blit(background,(0, 0))
        #window.blit(
        #font1.render('Пропущено: ' + str(ufo_miss), 1, (255, 255, 255)),(10, 10))

        player1.update_r() 
        player2.update_l()
        ball.run()
        ball.reset()
        player1.reset()
        player2.reset()
        


        win()

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
            ball.speed_y *= -1

        
        

    display.update()
    clock.tick(FPS)