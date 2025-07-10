from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, width=2)
    
    def update(self, dt):
        self.x += self.velocity * dt
        self.y += self.velocity * dt

