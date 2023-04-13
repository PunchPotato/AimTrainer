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
count_mouse_click_easy = 0
count_mouse_click_normal = 0
count_mouse_click_hard = 0
hit_easy = 0
hit_normal = 0
hit_hard = 0
screen = pygame.display.set_mode((width, height))
screen.fill("White")
bg = pygame.image.load("background/wood_surface_texture_118443_1920x1080.jpg").convert_alpha()
pygame.display.set_caption("AimTrainer")
white = (255, 255, 255)
blue = (0, 0, 128)
pygame.font.get_fonts()
current_time_reset_easy = pygame.time.get_ticks()
current_time_reset_normal = pygame.time.get_ticks()
current_time_reset_hard = pygame.time.get_ticks()
current_time_easy = pygame.time.get_ticks()
current_time_normal = pygame.time.get_ticks()
current_time_hard = pygame.time.get_ticks()
randomize_counter_easy = 0
randomize_counter_normal = 0
randomize_counter_hard = 0
easy_accuracy = 0
normal_accuracy = 0
hard_accuracy = 0


def get_font(size):
    return pygame.font.SysFont("consolas", size, bold=True)


def play():
    def difficulty_menu():
        while True:
            screen.blit(bg, (0, 0))

            DMENU_MOUSE_POS = pygame.mouse.get_pos()

            DMENU_TEXT = get_font(100).render("DIFFICULTY", True, (250, 250, 250))
            DMENU_RECT = DMENU_TEXT.get_rect(center=(640, 100))

            EASY_BUTTON = Button(image=pygame.image.load("button/button sign but cool.png"), pos=(640, 250),
                                 text_input="EASY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            NORMAL_BUTTON = Button(image=pygame.image.load("button/button sign but cool.png"), pos=(640, 400),
                                   text_input="NORMAL", font=get_font(75), base_color="#d7fcd4",
                                   hovering_color="White")
            HARD_BUTTON = Button(image=pygame.image.load("button/button sign but cool.png"), pos=(640, 550),
                                 text_input="HARD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            screen.blit(DMENU_TEXT, DMENU_RECT)

            for button in [EASY_BUTTON, NORMAL_BUTTON, HARD_BUTTON]:
                button.changeColor(DMENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_BUTTON.checkForInput(DMENU_MOUSE_POS):
                        easy()
                    if NORMAL_BUTTON.checkForInput(DMENU_MOUSE_POS):
                        normal()
                    if HARD_BUTTON.checkForInput(DMENU_MOUSE_POS):
                        hard()

            pygame.display.update()

    difficulty_menu()


def easy():
    class CIRCLE:

        def __init__(self):
            self.pos = None
            self.y = None
            self.x = None
            self.randomize()

        def draw_circle(self):
            global hit_easy
            global count_mouse_click_easy
            global easy_accuracy
            if hit_easy and count_mouse_click_easy >= 1:
                easy_accuracy = round(hit_easy / count_mouse_click_easy * 100, 1)
            text = get_font(70).render(str(f"ACCURACY: {easy_accuracy}%"), True, white)
            text_rect = text.get_rect()
            text_rect.center = (width // 2.4, height // 14)
            screen.blit(text, text_rect)
            time_text = get_font(70).render(str(f"TIME: {round(current_time_easy / 100, 1)}s"), True, white)
            time_text_rect = time_text.get_rect()
            time_text_rect.center = (width // 1.19, height // 14)
            screen.blit(time_text, time_text_rect)
            if easy_accuracy <= 50 and current_time_easy >= 399:
                end_screen_easy()

            screen.blit(drawn_circle, (self.x, self.y))

        def randomize(self):
            global randomize_counter_easy
            self.x = random.randint(50, 1230)
            self.y = random.randint(100, 670)
            self.pos = Vector2(self.x, self.y)
            randomize_counter_easy += 1

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            global hit_easy
            global count_mouse_click_easy
            global drawn_circle
            drawn_circle_rect = screen.blit(drawn_circle, (self.x, self.y))
            left_click = pygame.mouse.get_pressed()[0]
            circle_click = drawn_circle_rect
            if left_click and circle_click.collidepoint(mouse_pos):
                count_mouse_click_easy += 1
                hit_easy += 1
                self.__init__()
            else:
                count_mouse_click_easy += 1

    global count_mouse_click_easy
    global current_time_easy
    global current_time_reset_easy
    global randomize_counter_easy
    circle = CIRCLE()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_BACK = Button(image=None, pos=(100, 50),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        current_time_reset_easy += 1
        current_time_easy += 1

        if randomize_counter_easy >= 60:
            win_screen_easy()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circle.check_click()
                    circle.randomize()
                    current_time_reset_easy = 1
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        if current_time_reset_easy % 200 == 0:
            circle.check_click()
            circle.randomize()
            current_time_reset_easy = 1

        screen.blit(bg, (0, 0))
        PLAY_BACK.update(screen)
        circle.draw_circle()
        pygame.display.update()
        clock.tick(60)


def normal():
    class CIRCLE:

        def __init__(self):
            self.pos = None
            self.y = None
            self.x = None
            self.randomize()

        def draw_circle(self):
            global hit_normal
            global count_mouse_click_normal
            global normal_accuracy
            if hit_normal and count_mouse_click_normal >= 1:
                normal_accuracy = round(hit_normal / count_mouse_click_normal * 100, 1)
            text = get_font(70).render(str(f"ACCURACY: {normal_accuracy}%"), True, white)
            text_rect = text.get_rect()
            text_rect.center = (width // 2.4, height // 14)
            screen.blit(text, text_rect)
            time_text = get_font(70).render(str(f"TIME: {round(current_time_normal / 100, 1)}s"), True, white)
            time_text_rect = time_text.get_rect()
            time_text_rect.center = (width // 1.19, height // 14)
            screen.blit(time_text, time_text_rect)
            if normal_accuracy <= 60 and current_time_normal >= 299:
                end_screen_normal()

            screen.blit(drawn_circle, (self.x, self.y))

        def randomize(self):
            global randomize_counter_normal
            self.x = random.randint(50, 1230)
            self.y = random.randint(100, 670)
            self.pos = Vector2(self.x, self.y)
            randomize_counter_normal += 1

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            global hit_normal
            global count_mouse_click_normal
            global drawn_circle
            drawn_circle_rect = screen.blit(drawn_circle, (self.x, self.y))
            left_click = pygame.mouse.get_pressed()[0]
            circle_click = drawn_circle_rect
            if left_click and circle_click.collidepoint(mouse_pos):
                count_mouse_click_normal += 1
                hit_normal += 1
                self.__init__()
            else:
                count_mouse_click_normal += 1

    global count_mouse_click_normal
    global current_time_reset_normal
    global current_time_normal
    global randomize_counter_normal
    circle = CIRCLE()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_BACK = Button(image=None, pos=(100, 50),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        current_time_reset_normal += 1
        current_time_normal += 1

        if randomize_counter_normal >= 60:
            win_screen_normal()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circle.check_click()
                    circle.randomize()
                    current_time_reset_normal = 1
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    current_time_normal = 1
        if current_time_reset_normal % 140 == 0:
            circle.check_click()
            circle.randomize()
            current_time_reset_normal = 1

        screen.blit(bg, (0, 0))
        PLAY_BACK.update(screen)
        circle.draw_circle()
        pygame.display.update()
        clock.tick(60)


def hard():
    class CIRCLE:

        def __init__(self):
            self.pos = None
            self.y = None
            self.x = None
            self.randomize()

        def draw_circle(self):
            global hit_hard
            global count_mouse_click_hard
            global hard_accuracy
            if hit_hard and count_mouse_click_hard >= 1:
                hard_accuracy = round(hit_hard / count_mouse_click_hard * 100, 1)
            text = get_font(70).render(str(f"ACCURACY: {hard_accuracy}%"), True, white)
            text_rect = text.get_rect()
            text_rect.center = (width // 2.4, height // 14)
            screen.blit(text, text_rect)
            time_text = get_font(70).render(str(f"TIME: {round(current_time_hard / 100, 1)}s"), True, white)
            time_text_rect = time_text.get_rect()
            time_text_rect.center = (width // 1.19, height // 14)
            screen.blit(time_text, time_text_rect)
            if hard_accuracy <= 60 and current_time_hard >= 299:
                end_screen_hard()
                exit(hard())

            screen.blit(drawn_circle, (self.x, self.y))

        def randomize(self):
            global randomize_counter_hard
            self.x = random.randint(50, 1230)
            self.y = random.randint(100, 670)
            self.pos = Vector2(self.x, self.y)
            randomize_counter_hard += 1

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            global hit_hard
            global count_mouse_click_hard
            global drawn_circle
            drawn_circle_rect = screen.blit(drawn_circle, (self.x, self.y))
            left_click = pygame.mouse.get_pressed()[0]
            circle_click = drawn_circle_rect
            if left_click and circle_click.collidepoint(mouse_pos):
                count_mouse_click_hard += 1
                hit_hard += 1
                self.__init__()
            else:
                count_mouse_click_hard += 1

    global count_mouse_click_hard
    global current_time_reset_hard
    global current_time_hard
    global randomize_counter_hard
    circle = CIRCLE()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_BACK = Button(image=None, pos=(100, 50),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        current_time_reset_hard += 1
        current_time_hard += 1

        if randomize_counter_hard >= 60:
            win_screen_hard()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circle.check_click()
                    circle.randomize()
                    current_time_reset_hard = 1
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    current_time_hard = 1
                    exit(hard())
        if current_time_reset_hard % 60 == 0:
            circle.check_click()
            circle.randomize()
            current_time_reset_hard = 1

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

        MENU_TEXT = get_font(100).render("MAIN MENU", True, (250, 250, 250))
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


def end_screen_easy():
    while True:
        END_SCREEN_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        END_TEXT = get_font(75).render("You lost LOSER!", True, "White")
        END_RECT = END_TEXT.get_rect(center=(640, 260))
        screen.blit(END_TEXT, END_RECT)
        END_TEXT_2 = get_font(75).render(f"Your accuracy dropped to {easy_accuracy}%", True, "White")
        END_RECT_2 = END_TEXT_2.get_rect(center=(640, 360))
        screen.blit(END_TEXT_2, END_RECT_2)

        END_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        END_BACK.changeColor(END_SCREEN_MOUSE_POS)
        END_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if END_BACK.checkForInput(END_SCREEN_MOUSE_POS):
                    main_menu()
                    exit(end_screen_easy())

        pygame.display.update()


def end_screen_normal():
    while True:
        END_SCREEN_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        END_TEXT = get_font(75).render("You lost LOSER!", True, "White")
        END_RECT = END_TEXT.get_rect(center=(640, 260))
        screen.blit(END_TEXT, END_RECT)
        END_TEXT_2 = get_font(75).render(f"Your accuracy dropped to {normal_accuracy}%", True, "White")
        END_RECT_2 = END_TEXT_2.get_rect(center=(640, 360))
        screen.blit(END_TEXT_2, END_RECT_2)

        END_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        END_BACK.changeColor(END_SCREEN_MOUSE_POS)
        END_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if END_BACK.checkForInput(END_SCREEN_MOUSE_POS):
                    main_menu()
                    exit(end_screen_easy())

        pygame.display.update()


def end_screen_hard():
    while True:
        END_SCREEN_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        END_TEXT = get_font(75).render("You lost LOSER!", True, "White")
        END_RECT = END_TEXT.get_rect(center=(640, 260))
        screen.blit(END_TEXT, END_RECT)
        END_TEXT_2 = get_font(75).render(f"Your accuracy dropped to {hard_accuracy}%", True, "White")
        END_RECT_2 = END_TEXT_2.get_rect(center=(640, 360))
        screen.blit(END_TEXT_2, END_RECT_2)

        END_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        END_BACK.changeColor(END_SCREEN_MOUSE_POS)
        END_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if END_BACK.checkForInput(END_SCREEN_MOUSE_POS):
                    main_menu()
                    exit(end_screen_easy())

        pygame.display.update()


def win_screen_easy():
    while True:
        WIN_SCREEN_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        WIN_TEXT = get_font(75).render(f"TIME: {round(current_time_easy/ 100, 1)}s", True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 260))
        screen.blit(WIN_TEXT, WIN_RECT)
        WIN_TEXT_2 = get_font(75).render(f"ACCURACY: {round(easy_accuracy, 1)}%", True, "White")
        WIN_RECT_2 = WIN_TEXT_2.get_rect(center=(640, 360))
        screen.blit(WIN_TEXT_2, WIN_RECT_2)

        WIN_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        WIN_BACK.changeColor(WIN_SCREEN_MOUSE_POS)
        WIN_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_SCREEN_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def win_screen_normal():
    while True:
        WIN_SCREEN_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        WIN_TEXT = get_font(75).render(f"TIME: {round(current_time_normal/ 100, 1)}s", True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 260))
        screen.blit(WIN_TEXT, WIN_RECT)
        WIN_TEXT_2 = get_font(75).render(f"ACCURACY: {round(normal_accuracy, 1)}%", True, "White")
        WIN_RECT_2 = WIN_TEXT_2.get_rect(center=(640, 360))
        screen.blit(WIN_TEXT_2, WIN_RECT_2)

        WIN_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        WIN_BACK.changeColor(WIN_SCREEN_MOUSE_POS)
        WIN_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_SCREEN_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def win_screen_hard():
    while True:
        WIN_SCREEN_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        WIN_TEXT = get_font(75).render(f"TIME: {round(current_time_hard/ 100, 1)}s", True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 260))
        screen.blit(WIN_TEXT, WIN_RECT)
        WIN_TEXT_2 = get_font(75).render(f"ACCURACY: {round(hard_accuracy, 1)}%", True, "White")
        WIN_RECT_2 = WIN_TEXT_2.get_rect(center=(640, 360))
        screen.blit(WIN_TEXT_2, WIN_RECT_2)

        WIN_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        WIN_BACK.changeColor(WIN_SCREEN_MOUSE_POS)
        WIN_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_SCREEN_MOUSE_POS):
                    main_menu()

        pygame.display.update()


main_menu()
