import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')
img_player = pygame.image.load("Jet3.jpg")
img_player = pygame.transform.scale(img_player, (45,45))
img_player = pygame.transform.rotate(img_player, -90)
img_player_rect = img_player.get_rect()
img_player_rect.center = (400, 400)

#spaceship
img_ai = pygame.image.load("Spaceship.png")
img_ai = pygame.transform.scale(img_ai, (30,30))
img_ai = pygame.transform.rotate(img_ai, 90)
img_ai_rect = img_ai.get_rect()
img_ai_rect.center = (500, 400)

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 20


class PlaneGame:
    
    def __init__(self, w=850, h=500):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Planegame')
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.plane = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
      
        self.score = 0
        
        
    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:# moves the plane
                if event.key == pygame.K_a:
                  if self.head.x > 0:
                    self.direction = Direction.LEFT
                    self._move(self.direction) # update the head
                    self.plane.insert(0, self.head)
                elif event.key == pygame.K_d:
                  if self.head.x < 810:
                    self.direction = Direction.RIGHT
                    self._move(self.direction) # update the head
                    self.plane.insert(0, self.head)
                elif event.key == pygame.K_w:
                  if self.head.y > 0:
                    self.direction = Direction.UP
                    self._move(self.direction) # update the head
                    self.plane.insert(0, self.head)
                elif event.key == pygame.K_s:
                  if self.head.y < 450:
                    self.direction = Direction.DOWN
                    self._move(self.direction) # update the head
                    self.plane.insert(0, self.head)

                
                

        # 3. check if game over
        game_over = False

            
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return game_over, self.score
    
        
        
    def _update_ui(self):
        self.display.fill(WHITE)

        # self.display.blit(img_player, img_player_rect)
        self.display.blit(img_player, (self.head.x, self.head.y))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])


        pygame.display.flip()
        
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
        
    
     
if __name__ == '__main__':
    game = PlaneGame()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        
        if game_over == True:
            break
        
    print('Final Score', score)
        
        
    pygame.quit()