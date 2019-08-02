import pygame, sys
import random

class Runner():
    __customes = ('orange', 'red')
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint (0, 1)
        self.custome = pygame.image.load("images/{}.jpg".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    
    runners = []
    __posY = (200, 280)
    __names = ("DKchivu DKchivu DKchivaK", "las espinacas se machacan")
    __startLine = -10
    __finishLine = 620
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.jpg")
        
        #firstRunner = Runner (self.__startLine,0)
        #runners.append(firstRunner)
        
        for i in range(2):
            self.runners.append(Runner(self.__startLine, self.__posY[i]))
            self.runners[i].name = self.__names[i]
    
    def close(self):
        pygame.quit()
        sys.exit()
    
    
    def competir(self):
        
        
        gameOver = False
        
        while not gameOver:
            # comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                                        
            
            for runner in self.runners:
                runner.avanzar()
                
                if runner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(runner.name))
                    gameOver = True
                                
            
            # refrescar/renderizar la pantalla
            self.__screen.blit(self.background, (0,0))
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
        
    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()