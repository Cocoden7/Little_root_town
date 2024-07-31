import random

import pygame


class Particle:
    def __init__(self, vx, vy, radius, initial_position=(150, 150), color=(255, 255, 255)):
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.pos = list(initial_position)
        self.color = color

    def update(self):
        self.pos[0] += self.vx
        self.pos[1] += self.vy
        self.radius -= 0.002

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.pos[0]), int(self.pos[1])], self.radius)


class ParticleSystem:
    def __init__(self, ):
        self.particles = []
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter > 1000:
            self.particles.append(Particle(random.choice([-1, 1])*random.random()/400, 0.0075, 4))
            self.counter = 0
        for p in self.particles:
            p.update()
        if len(self.particles) > 100:
            del self.particles[0]

    def draw(self, screen):
        for p in self.particles:
            p.draw(screen)


if __name__ == '__main__':
    clock = pygame.time.Clock()
    res=(300, 300)
    screen = pygame.display.set_mode(res)
    count = 0
    particles = []
    ps = ParticleSystem()
    move = False
    while True:
        clock.tick(1500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move = False
        screen.fill((0, 0, 0))
        if move:
            ps.update()
            ps.draw(screen)
        pygame.display.update()

