import pygame

# plan = []
# for y in range(100):
#     plan.append([])
#     for x in range(100):
#         plan[-1].append()

SIZE = WIDTH, HEIGHT = (640, 400)
CELL = 10

def add(points):
    last = points[-1]
    print(last)
    if last.imag > 0 and last.real == 0:
        print(last)
        point = last.real + 1 + last.imag
    else:
    #     point = last.real + 1 + last.imag
        point = last * 1j
    points.append(point)

def render(points, screen):
    for p in points:
        rect = pygame.Rect(p.real * CELL + WIDTH // 2,
                           -p.imag * CELL + HEIGHT // 2, 0, 0)
        rect.width = rect.height = CELL
        if p == 0:
            color = pygame.Color('red')
        else:
            color = pygame.Color('grey')
        pygame.draw.rect(screen, color, rect)

screen = pygame.display.set_mode((640, 400))

def main():
    points = [0, 1j]
    render(points, screen)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                add(points)
                render(points, screen)
        pygame.display.flip()


main()
