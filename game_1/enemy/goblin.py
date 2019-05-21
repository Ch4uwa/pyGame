import pygame


class Enemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [0, 500]
        self.path_pos = 0
        self.animation_count = 0
        self.move_count = 0
        self.vel = 3
        self.img = None
        self.health = 5
        self.dead = False
        self.visible = True
        # self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    walkRight = [pygame.image.load('res/enemy/R1E.png'),
                 pygame.image.load('res/enemy/R2E.png'),
                 pygame.image.load('res/enemy/R3E.png'),
                 pygame.image.load('res/enemy/R4E.png'),
                 pygame.image.load('res/enemy/R5E.png'),
                 pygame.image.load('res/enemy/R6E.png'),
                 pygame.image.load('res/enemy/R7E.png'),
                 pygame.image.load('res/enemy/R8E.png'),
                 pygame.image.load('res/enemy/R9E.png'),
                 pygame.image.load('res/enemy/R10E.png'),
                 pygame.image.load('res/enemy/R11E.png')]

    walkLeft = [pygame.image.load('res/enemy/L1E.png'),
                pygame.image.load('res/enemy/L2E.png'),
                pygame.image.load('res/enemy/L3E.png'),
                pygame.image.load('res/enemy/L4E.png'),
                pygame.image.load('res/enemy/L5E.png'),
                pygame.image.load('res/enemy/L6E.png'),
                pygame.image.load('res/enemy/L7E.png'),
                pygame.image.load('res/enemy/L8E.png'),
                pygame.image.load('res/enemy/L9E.png'),
                pygame.image.load('res/enemy/L10E.png'),
                pygame.image.load('res/enemy/L11E.png')]

    # def resetPos(self):
    #     self.x = (screen_width - self.width / 2)
    #     self.y = 410
    #     self.walkCount = 0

    def draw(self, window):
        """ Draw the enemy with given image """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        """
        self.move()
        if not self.dead:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount // 3],
                            (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount // 3],
                            (self.x, self.y))
                self.walkCount += 1

            # Healthbar
            pygame.draw.rect(window, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1] -
                              20, 50, 10))

            pygame.draw.rect(window, (0, 255, 0),
                             (self.hitbox[0], self.hitbox[1] -
                              20, (5 * self.health), 10))

            self.hitbox = (self.x + 22, self.y + 5, 31, 52)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
            """

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        elif self.health <= 0:
            self.deaths += 1

            i = 0
            while i < 300:
                pygame.time.wait(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
