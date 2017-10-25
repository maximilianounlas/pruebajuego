import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode([900,600])
    fondo='C:\Users\maxi\Desktop/Running1.PNG' #carga de fondo
    pygame.display.set_caption("prueba")
    rojo=(200,40,100)
    color1=(255,255,255)
    s2=pygame.Surface((10,50))
    s1=pygame.image.load(fondo).convert_alpha()
    clock = pygame.time.Clock()#
    salir=False
    s3=pygame.transform.smoothscale(s1,(100,200))
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
        clock.tick_busy_loop(30)
        screen.fill(rojo)
        screen.blit(s3,(1,40))
        screen.blit(s1,(500,100))
        pygame.display.update()
    pygame.quit()
main()