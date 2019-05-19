import pygame
import random
pygame.init()


bg = pygame.image.load('res/bg.jpg')
char = pygame.image.load('res/player/standing.png')

clock = pygame.time.Clock()

screen_width = 500
screen_height = 480
font = pygame.font.SysFont("arial", 20, True)

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Crazy Game")

bulletSound = pygame.mixer.Sound("res/sound/bullet.wav")
hitSound = pygame.mixer.Sound("res/sound/hit.wav")

music = pygame.mixer.music.load("res/sound/music.mp3")
pygame.mixer.music.play(-1)


class player:

    walkRight = [pygame.image.load('res/player/R1.png'),
                 pygame.image.load('res/player/R2.png'),
                 pygame.image.load('res/player/R3.png'),
                 pygame.image.load('res/player/R4.png'),
                 pygame.image.load('res/player/R5.png'),
                 pygame.image.load('res/player/R6.png'),
                 pygame.image.load('res/player/R7.png'),
                 pygame.image.load('res/player/R8.png'),
                 pygame.image.load('res/player/R9.png')]

    walkLeft = [pygame.image.load('res/player/L1.png'),
                pygame.image.load('res/player/L2.png'),
                pygame.image.load('res/player/L3.png'),
                pygame.image.load('res/player/L4.png'),
                pygame.image.load('res/player/L5.png'),
                pygame.image.load('res/player/L6.png'),
                pygame.image.load('res/player/L7.png'),
                pygame.image.load('res/player/L8.png'),
                pygame.image.load('res/player/L9.png')]

    def __init__(self, pos_x, pos_y, width, height):
        self.name = "Berra"
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpHight = 10
        self.standing = True
        self.hitbox = (self.pos_x + 17, self.pos_y + 11, 29, 52)
        self.dead = False
        self.health = 10

    def resetPos(self):
        self.pos_x = (0 + self.width / 2)
        self.pos_y = 410
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
                                (self.pos_x, self.pos_y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(self.walkRight[self.walkCount // 3],
                                (self.pos_x, self.pos_y))
                    self.walkCount += 1
            else:
                if self.right:
                    window.blit(self.walkRight[0], (self.pos_x, self.pos_y))
                else:
                    window.blit(self.walkLeft[0], (self.pos_x, self.pos_y))

            self.hitbox = (self.pos_x + 17, self.pos_y + 11, 29, 52)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)


def save(filename):
    with open(filename, 'w') as f:
        f.write(p1.name + ";" + "Score" + str(enemies[0].deaths) +
                ";" + "Enemy speed" + ";" + str(abs(enemies[0].vel)))


class enemy:
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

    def __init__(self, pos_x, pos_y, end):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 64
        self.height = 64
        self.end = end
        self.path = [self.pos_x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.pos_x + 17, self.pos_y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.deaths = 0

    def resetPos(self):
        self.pos_x = (screen_width - self.width / 2)
        self.pos_y = 410
        self.walkCount = 0

    def draw(self, window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount // 3],
                            (self.pos_x, self.pos_y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount // 3],
                            (self.pos_x, self.pos_y))
                self.walkCount += 1

            # Healthbar
            pygame.draw.rect(window, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1] -
                              20, 50, 10))

            pygame.draw.rect(window, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] -
                              20, (5 * self.health), 10))

            self.hitbox = (self.pos_x + 22, self.pos_y + 5, 31, 52)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.pos_x + self.vel < self.path[0]:
                self.pos_x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.pos_x - self.vel > self.path[1]:
                self.pos_x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        elif self.health <= 0:
            self.visible = False
            self.pos_x = (screen_width - self.width / 2)
            self.deaths += 1
            p1.health += 1

            i = 0
            while i < 300:
                pygame.time.wait(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()

            self.visible = True
            self.health = 10
            self.health += self.deaths
            self.vel += self.deaths


class projectile:
    def __init__(self, pos_x, pos_y, radius, color, facing):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color,
                           (self.pos_x, self.pos_y), self.radius)


p1 = player(0, 410, 64, 64)
enemies = []
enemies.append(enemy((screen_width - 64), 410, 0))
shootLoop = 0
run = True
bullets = []


def redrawGamewindowdow():
    window.blit(bg, (0, 0))
    p1.draw(window)
    for e in enemies:
        e.draw(window)
    time = font.render("Score: " + str(enemies[0].deaths),
                       1, (0, 0, 0))
    text = font.render("Health: " + str(p1.health), 1, (0, 0, 0))
    window.blit(text, (5, 10))
    text1 = font.render("Health: " + str(enemies[0].health), 1, (0, 0, 0))
    window.blit(text1, ((screen_width - text1.get_width()), 10))
    window.blit(time, ((screen_width/2) - (time.get_width() / 2), 10))

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()


# Mainloop
while run:
    clock.tick(27)
    # pygame.time.get_ticks()
# Check collision if enemy touches player
    if (p1.hitbox[1] < enemies[0].hitbox[1] + enemies[0].hitbox[3] and
            p1.hitbox[1] + p1.hitbox[3] > enemies[0].hitbox[1]):
        if (p1.hitbox[0] + p1.hitbox[2] > enemies[0].hitbox[0] and
                p1.hitbox[0] < enemies[0].hitbox[0] + enemies[0].hitbox[2]):
            p1.hit()

# control how fast you shoot
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 2:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Check for bullet collision on enemy
    for bullet in bullets:
        if (bullet.pos_y - bullet.radius < enemies[0].hitbox[1] + enemies[0].hitbox[3] and
                bullet.pos_y + bullet.radius > enemies[0].hitbox[1]):
            if (bullet.pos_x + bullet.radius > enemies[0].hitbox[0] and
                    bullet.pos_x - bullet.radius <
                    enemies[0].hitbox[0] + enemies[0].hitbox[2]):

                enemies[0].hit()
                bullets.pop(bullets.index(bullet))

        if bullet.pos_x < screen_width and bullet.pos_x > 0:
            bullet.pos_x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0 and p1.left | p1.right:
        bulletSound.play()
        if p1.left:
            facing = -1
        elif p1.right:
            facing = 1

        if len(bullets) < 5:
            shootLoop += 1
            bullets.append(projectile(
                round(p1.pos_x + p1.width // 2),
                round(p1.pos_y + p1.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and p1.pos_x > p1.vel:
        p1.pos_x -= p1.vel
        p1.left = True
        p1.right = False
        p1.standing = False

    elif keys[pygame.K_RIGHT] and p1.pos_x < screen_width - p1.width - p1.vel:
        p1.pos_x += p1.vel
        p1.left = False
        p1.right = True
        p1.standing = False
    else:
        p1.walkCount = 0
        p1.standing = True

    if not(p1.isJump):
        if keys[pygame.K_UP]:
            p1.isJump = True
            p1.walkCount = 0
    else:
        if p1.jumpHight >= -10:
            neg = 1
            if p1.jumpHight < 0:
                neg = -1
            p1.pos_y -= (p1.jumpHight ** 2) * 0.5 * neg
            p1.jumpHight -= 1
        else:
            p1.isJump = False
            p1.jumpHight = 10

    redrawGamewindowdow()

pygame.quit()
