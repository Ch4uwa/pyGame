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
