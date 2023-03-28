import pygame
import random
from pygame.math import Vector2

width = 1920
height = 1080

pygame.init()
clock = pygame.time.Clock()


circle_Load = pygame.image.load("targets/working target.png")
drawn_circle = pygame.transform.scale(circle_Load, (55, 55))
count_mouse_click = 0
hit = 0
screen = pygame.display.set_mode((width, height))
screen.fill("White")
bg = pygame.image.load("background/wood_surface_texture_118443_1920x1080.jpg").convert_alpha()
pygame.display.set_caption("AimTrainer")
black = (0, 0, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)


class CIRCLE:
    def __init__(self):
        self.pos = None
        self.y = None
        self.x = None
        self.randomize()

    def draw_circle(self):
        global hit
        global count_mouse_click
        if hit and count_mouse_click >= 1:
            accuracy = round(hit / count_mouse_click * 100, 2)
            text = font.render(str(f"Your Accuracy Is: {accuracy}"), True, black)
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height // 2)
            screen.blit(text, text_rect)

        screen.blit(drawn_circle, (self.x, self.y))

    def randomize(self):
        self.x = random.randint(50, 1870)
        self.y = random.randint(50, 1030)
        self.pos = Vector2(self.x, self.y)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        global hit
        global count_mouse_click
        global drawn_circle
        drawn_circle_rect = screen.blit(drawn_circle, (self.x, self.y))
        left_click = pygame.mouse.get_pressed()[0]
        circle_click = drawn_circle_rect
        if left_click and circle_click.collidepoint(mouse_pos):
            count_mouse_click += 1
            hit += 1
            self.__init__()
        else:
            count_mouse_click += 1
            return False


circle = CIRCLE()
circle.draw_circle()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle.check_click()

    screen.blit(bg, (0, 0))
    circle.draw_circle()
    pygame.display.update()
    clock.tick(120)

