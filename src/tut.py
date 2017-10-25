import pygame
import random
pygame.init()
foodimg=pygame.image.load("C:\Users\maxi\Desktop/Running1.png")
foodrect=foodimg.get_rect()
white = (255,255,255)
#Game Display
display_width = 1080
display_height  = 720
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Click It! ~ Snapnel Productions')
gameDisplay.fill((white))
running=True
while running:
    gameDisplay.fill((white))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if foodrect.collidepoint(x, y):
                foodrect.center=(random.randint(5,1060),random.randint(5,700))
                print "Hi",
                continue 
    gameDisplay.blit(foodimg,foodrect)
    pygame.display.flip()