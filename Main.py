import pygame
import random
from pygame.math import Vector2

width = 1920
height = 1080
count_mouse_click = 0
hit = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AimTrainer")
screen.fill("White")

pygame.init()
clock = pygame.time.Clock()


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
            accuracy = hit / count_mouse_click * 100
            print(accuracy)
        else:
            print("eat shit")
        self.circle = pygame.draw.circle(screen, "Red", (self.x, self.y), 25)


    def randomize(self):
        self.x = random.randint(0, 1870)
        self.y = random.randint(0, 1030)
        self.pos = Vector2(self.x, self.y)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        global hit
        global count_mouse_click
        # accuracy = count_mouse_click / hit * 100
        left_click = pygame.mouse.get_pressed()[0]
        circle_click = pygame.draw.circle(screen, "Red", (self.x, self.y), 25)
        if left_click and circle_click.collidepoint(mouse_pos):
            count_mouse_click += 1
            hit += 1
            print(count_mouse_click)
            self.__init__()
        else:
            count_mouse_click += 1
            print(count_mouse_click)
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

    screen.fill((0, 0, 0))
    circle.draw_circle()
    pygame.display.update()
    clock.tick(120)
