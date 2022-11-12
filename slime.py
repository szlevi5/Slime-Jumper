import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Slime Jumper")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/font.ttf",50)

sky_surface = pygame.image.load("assets/sky.jpg")
ground_surface = pygame.image.load("assets/ground.jpg")
text_surface = test_font.render("SCORE:",True,"black")

slime_surface = pygame.image.load("assets/slime.jpg")
slime_x_pos = 700

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,320))
    screen.blit(text_surface, (300,20))
    slime_x_pos -= 10
    if slime_x_pos < -120: slime_x_pos = 800
    screen.blit(slime_surface,(slime_x_pos,220))

    pygame.display.update()
    clock.tick(60)