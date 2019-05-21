import pygame


class Player:
    def __init__(self, x, y, width, height, name):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpHight = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.dead = False
        self.score = 0
        self.health = 10

    walkRight = [pygame.image.load('R1.png'),
                 pygame.image.load('R2.png'),
                 pygame.image.load('R3.png'),
                 pygame.image.load('R4.png'),
                 pygame.image.load('R5.png'),
                 pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'),
                 pygame.image.load('R8.png'),
                 pygame.image.load('R9.png')]

    walkLeft = [pygame.image.load('res/player/L1.png'),
                pygame.image.load('res/player/L2.png'),
                pygame.image.load('res/player/L3.png'),
                pygame.image.load('res/player/L4.png'),
                pygame.image.load('res/player/L5.png'),
                pygame.image.load('res/player/L6.png'),
                pygame.image.load('res/player/L7.png'),
                pygame.image.load('res/player/L8.png'),
                pygame.image.load('res/Player/L9.png')]

    def resetPos(self):
        self.x = (0 + self.width / 2)
        self.y = 410
        self.walkCount = 0

    def hit(self):
        font1 = pygame.font.SysFont("arial", 50)
        text = font1.render("-5", 1, (255, 0, 0))
        window.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        enemies[0].resetPos()
        self.health -= 5
        pygame.time.wait(500)

        if self.health <= 0:
            self.dead = True
            self.text1 = font1.render("GAME OVER!", 1, (255, 0, 0))
            window.blit(self.text1, ((screen_width / 2) -
                                     (self.text1.get_width() / 2),
                                     (screen_height / 2)))
            pygame.display.update()
            save("savedgame.txt")
            pygame.time.wait(2000)
            self.health = 10
            self.resetPos()
            self.walkCount = 0
            self.dead = False
            enemies[0].resetPos()
            enemies[0].vel = 3

    def draw(self, window):
        if not self.dead:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not(self.standing):
                if self.left:
                    window.blit(self.walkLeft[self.walkCount // 3],
                                (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(self.walkRight[self.walkCount // 3],
                                (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    window.blit(self.walkRight[0], (self.x, self.y))
                else:
                    window.blit(self.walkLeft[0], (self.x, self.y))

            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)


def save(filename):
    with open(filename, 'a') as f:
        f.write(p1.name + ";" + "Score" + ";" + str(p1.score) + "\n")
