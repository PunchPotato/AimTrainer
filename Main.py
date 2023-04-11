import pygame
import random
from pygame.math import Vector2
from a import Button
import sys

width = 1280
height = 720

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
white = (255, 255, 255)
blue = (0, 0, 128)
pygame.font.get_fonts()
current_time = pygame.time.get_ticks()


def get_font(size):
    return pygame.font.SysFont("consolas", size, bold=True)


def play():
    class CIRCLE:

        def __init__(self):
            self.pos = None
            self.y = None
            self.x = None
            self.randomize()

        def draw_circle(self):
            global hit
            global count_mouse_click
            accuracy = 0
            if hit and count_mouse_click >= 1:
                accuracy = round(hit / count_mouse_click * 100, 1)
            text = get_font(75).render(str(f"ACCURACY: {accuracy}%"), True, white)
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height // 14)
            screen.blit(text, text_rect)

            screen.blit(drawn_circle, (self.x, self.y))

        def randomize(self):
            self.x = random.randint(50, 1230)
            self.y = random.randint(100, 670)
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

    global count_mouse_click
    global current_time
    circle = CIRCLE()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_BACK = Button(image=None, pos=(100, 50),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        print(current_time)
        current_time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circle.check_click()
                    circle.randomize()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        if current_time % 160 == 0:
            circle.check_click()
            circle.randomize()

        screen.blit(bg, (0, 0))
        PLAY_BACK.update(screen)
        circle.draw_circle()
        pygame.display.update()
        clock.tick(60)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(200, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("button/button sign but cool.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("button/button sign but cool.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("button/button sign but cool.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
