import pygame, sys
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/smallball.jpg")
        self.position = [x, y]
        self.name = "Bolita"
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    
    runners = []
    __startLine = -10
    __finishLine = 620
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.jpg")
        
        #firstRunner = Runner (self.__startLine,0)
        #runners.append(firstRunner)
        
        self.runners.append(Runner(self.__startLine, 240))
        self.runners[0].name = "dekachivu dekachivu dekachivaka"
    
    def competir(self):
        
        
        gameOver = False
        
        while not gameOver:
            # comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    pygame.quit()
                    sys.exit()
            
            self.runners[0].avanzar()
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado".format(self.runners[0].name))
                gameOver = True
                
            # refrescar/renderizar la pantalla
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            pygame.display.flip()
             
    
    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()