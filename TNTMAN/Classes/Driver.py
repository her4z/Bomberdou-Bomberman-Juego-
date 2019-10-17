import Map
import pygame
import Background


class Driver:
    def __init__(self):
        self.dimentions = (800, 600)
        self.map = Map.Map(self.dimentions)
        self.view = pygame.display.set_mode(self.dimentions)
        self.caption = pygame.display.set_caption("TNTMan")
        self.bUnbreakable = pygame.image.load("background.jpg")
        self.view.blit(self.bUnbreakable, (0, 0))
        self.main_loop()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.map.move_tm(CONTROLS[str(event.key)])
                    self.view.reload_background()
                    self.view.reload_tntman()
                # self.view.fill([255, 255, 255])
                pygame.display.flip()
        
    def block_load(self):  
        self.bUnbreakable = pygame.image.load("bUnbreakable32x32.png")
        self.view.blit(self.bUnbreakable, (17, 29))


if __name__ == "__main__":
    driver = Driver()
    Background = Background("background.jpg", [0, 0])