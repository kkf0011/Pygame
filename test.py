import pygame
import sys
from pygame.locals import *
import  math
from random import *

Score = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
icon = pygame.image.load("LOGO.png")
pygame.display.set_icon(icon)
bg_size = width, height = 1200, 900
clock = pygame.time.Clock()
pygame.display.set_caption("YYJDXM")
screen = pygame.display.set_mode(bg_size)



def msg(txt,color,size,x,y):
    font=pygame.font.SysFont("comicsansms",size,bold=1)
    mtxt=font.render(txt,True,color)
    mrect=mtxt.get_rect()
    mrect.center=x,y
    screen.blit(mtxt, mrect)


class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -(self.speed[0]  - 5)
            self.score += 1
            if self.rect.right > width and self.rect.right + self.speed[0] > self.rect.right:
                self.speed[0] = -(self.speed[0] + 5 )
                self.score += 1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -(self.speed[1] - 7)
            self.score += 1
            if self.rect.bottom > height and self.rect.bottom + self.speed[1] > self.rect.bottom:
                self.speed[1] = -(self.speed[1] + 7)
                self.score += 1



def collide(item, target):
    distance = math.sqrt(
        math.pow((item.rect.center[0] - target.rect.center[0]), 2) +
        math.pow((item.rect.center[1] - target.rect.center[1]), 2))
    if distance <= (item.rect.width + target.rect.width) / 2:
        return True

def gameover(Score):
    wait=1
    while wait:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    wait=0
        screen.fill(WHITE)
        msg("Score:" + str(Score), BLACK, 50, 600, 600)
        msg("Game Over",BLACK ,50,600,400)
        pygame.display.update()

def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("新学期スタート！.ogg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()

    bomb_image = "bomb1.png"
    yyj_image = "YYJ.png"
    bg_image = "background.png"

    running = True
    background = pygame.image.load(bg_image).convert_alpha()

    yyjs = []
    ygroup = pygame.sprite.Group()

    for i in range(1):
        yyj_position = 0,0
        yyj_speed = [3,3]
        yyj = Ball(yyj_image, yyj_position, yyj_speed, bg_size)
        yyjs.append(yyj)
        ygroup.add(yyj)

    bombs = []
    bgroup = pygame.sprite.Group()
    for i in range(1):
        bomb_position = 1000, 800
        bomb_speed = [1, 1]
        bomb = Ball(bomb_image, bomb_position,bomb_speed, bg_size)
        bombs.append(bomb)
        bgroup.add(bomb)




    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    yyj.speed[0] = yyj.speed[0] - 1 if yyj.speed[0] < 0 else yyj.speed[0] - 1
                elif event.key == pygame.K_d:
                    yyj.speed[0] = yyj.speed[0] + 1 if yyj.speed[0] > 0 else yyj.speed[0] + 1
                elif event.key == pygame.K_w:
                    yyj.speed[1] = yyj.speed[1] - 1 if yyj.speed[1] > 0 else yyj.speed[1] - 1
                elif event.key == pygame.K_x:
                    yyj.speed[1] = yyj.speed[1] + 1 if yyj.speed[1] < 0 else yyj.speed[1] + 1
                elif event.key == pygame.K_LEFT:
                    bomb.speed[0] = bomb.speed[0] - 1 if bomb.speed[0] < 0 else bomb.speed[0] - 1
                elif event.key == pygame.K_RIGHT:
                    bomb.speed[0] = bomb.speed[0] + 1 if bomb.speed[0] > 0 else bomb.speed[0] + 1
                elif event.key == pygame.K_UP:
                    bomb.speed[1] = bomb.speed[1] - 1 if bomb.speed[1] > 0 else bomb.speed[1] - 1
                elif event.key == pygame.K_DOWN:
                    bomb.speed[1] = bomb.speed[1] + 1 if bomb.speed[1] < 0 else bombs.speed[1] + 1
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
        if collide(yyj,bomb):
            gameover(Score)
        screen.blit(background, (0, 0))
        for each in yyjs:
            each.move()
            screen.blit(each.image, each.rect)
        for each in bombs:
            each.move()
            screen.blit(each.image, each.rect)
        Score = yyj.score + bomb.score
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
