import pygame

size = 30

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def is_prime(x, y):
    if 0 in (x, y):
        return False
    return gcd(x, y) == 1

plane = []

for y in range(size):
    plane.append([])
    for x in range(size):
        # x -= size // 2
        # y -= size // 2
        p = int(is_prime(x, y)) * 255
        plane[-1].append([p, p, p])

def mainloop(plane):
    screen = pygame.display.set_mode((size, size))
    surf = pygame.surfarray.make_surface(plane)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        screen.blit(surf, (0, 0))
        pygame.display.flip()

mainloop(plane)
