import pygame

from pygame import FULLSCREEN

"""
    MORPION
"""

pygame.init()

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN)

running = True

grille_image = pygame.image.load("Grille.png")
croix_image = pygame.image.load("Croix.png")
rond_image = pygame.image.load("Rond.png")

tour = 0

bouton_enfonce = False


def grille():
    screen.blit(grille_image, (0, 0))


def croix(x, y):
    screen.blit(croix_image, (x, y))


def rond(x, y):
    screen.blit(rond_image, (x, y))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if pygame.mouse.get_pressed()[0] and not bouton_enfonce:

            bouton_enfonce = True
            if 0 < pygame.mouse.get_pos()[0] < 640 and 0 < pygame.mouse.get_pos()[1] < 640:  # Si la souris est enfoncée

                if tour == 0:
                    rond(0, 0)
                    tour = 1
                else:
                    croix(0, 0)
                    tour = 0

        if pygame.mouse.get_pressed()[1]:
            bouton_enfonce = False

    grille()

    pygame.display.update()
