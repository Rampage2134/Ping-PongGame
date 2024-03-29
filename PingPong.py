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

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass




window = display.set_mode((700, 500))
display.set_caption("Ping - Pong")
background = transform.scale(image.load("images.jpg"), (700, 500))
clock = time.Clock()

font.init()
font2 = font.SysFont("Arial", 42)
font3 = font.SysFont("Arial", 72)

player1 = Player1("Ракетка.png", 50, 250, 10, 20, 65)
player2 = Player2("Ракетка.png", 650, 250, 10, 20, 65)
ball = Ball("Remove-bg.ai_1711727554450.png", 325, 250, 7, 50, 50)

game = True
finish = False

while game:

    for e in event.get(): 
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()


    display.update()
    clock.tick(60)
