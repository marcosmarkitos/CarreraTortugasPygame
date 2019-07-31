import pygame
import sys

class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.jpg")
        
        self.runner = pygame.image.load("images/smallball.jpg")
    
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            # comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # refrescar/renderizar la pantalla
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                hayGanador = True

   
    
    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()