import pygame
import os
from enemys.goblin import Goblin


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Goblin()]
        self.clicks = []
        self.bg = pygame.image.load(os.path.join('game_assets', 'bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(mouse_pos)
                    print(mouse_pos)

            # Loop through enemies
            to_del = []
            for en in self.enemies:
                if en.health <= 0:
                    to_del.append(en)

            for d in to_del:
                pass

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        for p in self.clicks:
            pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)
        pygame.display.update()


if __name__ == "__main__":
    g = Game()
    g.run()
"""
def redrawGamewindowdow():
    window.blit(bg, (0, 0))
    p1.draw(window)
    for e in enemies:
        e.draw(window)
    time = font.render("Score: " + str(p1.score),
                       1, (0, 0, 0))
    text = font.render("Health: " + str(p1.health), 1, (0, 0, 0))
    window.blit(text, (5, 10))

    window.blit(time, ((screen_width/2) - (time.get_width() / 2), 10))

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()


# Mainloop
while run:
    clock.tick(27)
    # pygame.time.get_ticks()

    if len(enemies) == 0:
        enemies.append(enemy(Random().randrange(0, (screen_width - 64)), 410, 0))
    elif len(enemies) < p1.score:
        enemies.append(enemy(Random().randrange(0, (screen_width - 64)), 410, 0))

# Check collision if enemy touches player
    if (p1.hitbox[1] < enemies[0].hitbox[1] + enemies[0].hitbox[3] and
            p1.hitbox[1] + p1.hitbox[3] > enemies[0].hitbox[1]):
        if (p1.hitbox[0] + p1.hitbox[2] > enemies[0].hitbox[0] and
                p1.hitbox[0] < enemies[0].hitbox[0] + enemies[0].hitbox[2]):
            p1.hit()

# control how fast you shoot
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Check for bullet collision on enemy
    for bullet in bullets:
        for e in enemies:
            if (bullet.pos_y - bullet.radius < e.hitbox[1] +
                    e.hitbox[3] and
                    bullet.pos_y + bullet.radius > e.hitbox[1]):
                if (bullet.pos_x + bullet.radius > e.hitbox[0] and
                        bullet.pos_x - bullet.radius <
                        e.hitbox[0] + e.hitbox[2]):

                    e.hit()
                    bullets.pop(bullets.index(bullet))

        if bullet.pos_x < screen_width and bullet.pos_x > 0:
            bullet.pos_x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if len(enemies) <= 5 and not 0:
        for e in enemies:
            if e.health <= 0:
                enemies.pop(enemies.index(e))
                p1.score += 1

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
"""
