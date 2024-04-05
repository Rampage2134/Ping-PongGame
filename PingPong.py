from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pic, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pic), (size_x, size_y))
        self.rect = self.image.get_rect(x = x, y = y)
        self.speed = speed

    def reset(self):
        window.blit(self.image, self.rect)
    
    def collide(self, other):
        return self.rect.colliderect(other.rect)


class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
        

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed
        

class Ball(GameSprite):
    def update(self):
        pass




window = display.set_mode((700, 500))
display.set_caption("Ping - Pong")
background = transform.scale(image.load("images.jpg"), (700, 500))
clock = time.Clock()

score1 = 0
score2 = 0

font.init()
font2 = font.SysFont("Arial", 35)
font3 = font.SysFont("Arial", 72)

font_score1 = font2.render("Счет первого игрока:" + str(score1), True, (0, 0, 0))
font_score2 = font2.render("Счет второго игрока:" + str(score2), True, (0, 0, 0))
font_win1 = font3.render("Player1 WIN!!!", True, (0, 0, 0))
font_win2 = font3.render("Player1 WIN!!!", True, (0, 0, 0))

player1 = Player1("Ракетка.png", 50, 250, 10, 20, 65)
player2 = Player2("Ракетка.png", 650, 250, 10, 20, 65)
ball = Ball("Remove-bg.ai_1711727554450.png", 325, 250, 7, 50, 50)

speed_x = 3
speed_y = 3

game = True
finish = False

while game:

    for e in event.get(): 
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        window.blit(font_score1, (20, 30))
        window.blit(font_score2, (380, 30))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        score1 += 1
        font_score1 = font2.render("Счет первого игрока:" + str(score1), True, (0, 0, 0))
        ball.rect.x = 325

    if ball.rect.x > 700:
        score2 += 1
        font_score2 = font2.render("Счет второго игрока:" + str(score2), True, (0, 0, 0))
        ball.rect.x = 325

    if score1 == 5:
        window.blit(font_win1, (150, 220))
        finish = True

    if score2 == 5:
        window.blit(font_win2, (150, 220))
        finish = True


    display.update()
    clock.tick(60)
