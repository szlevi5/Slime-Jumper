import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Slime Jumper")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/font.ttf",50)



sky_surf = pygame.image.load("assets/sky.jpg").convert_alpha()
ground_surf = pygame.image.load("assets/ground.jpg").convert_alpha()
text_surf = test_font.render("SCORE:",True,"black")

enemy_surf = pygame.image.load("assets/slime.jpg").convert_alpha()
enemy_rect = enemy_surf.get_rect(bottomright = (700,320))

player_surf = pygame.image.load("assets/player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (150,320))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #bakground#
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf, (0,320))
    screen.blit(text_surf, (300,20))
    
    #enemy#
    enemy_rect.x -= 13
    if enemy_rect.right <= 0: enemy_rect.left = 800
    screen.blit(enemy_surf,enemy_rect)
    
    #player#
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)