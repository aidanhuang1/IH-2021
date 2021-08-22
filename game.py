import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.SysFont('arial', 25)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 40
bullets = []

img_player = pygame.image.load("Jet3.jpg")
img_player = pygame.transform.scale(img_player, (45, 45))
img_player = pygame.transform.rotate(img_player, -90)


class projectile(object):
    def __init__(self, x, y):
        self.x = 900
        self.y = random.randint(50, 550)

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), 10)


class Game:
    def __init__(self, w=1000, h=600):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(100, self.h / 2)
        self.snake = [self.head]
        self.score = 0
        self.food = None
        self.frame_iteration = 0
        bullets.clear()

    def play_step(self, action):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # moves the plane
                if event.key == pygame.K_w:
                    if self.head.y > 0:
                        self.direction = Direction.RIGHT
                        self._move(self.direction)  # update the head
                if event.key == pygame.K_s:
                    if self.head.y < 450:
                        self.direction = Direction.LEFT
                        self._move(self.direction)  # update the head
                if event.key == pygame.K_x:
                    if len(bullets) < 20:
                        bullets.append(projectile(self.head.x, self.head.y))

                        # 3. check if game over
        game_over = False
        reward = 10
        # 5. update ui and clock

        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        for bullet in bullets:
            if bullet.x == self.head.x and bullet.y == self.head.y:
                return True
        return False

    def _update_ui(self):
        self.display.fill(BLACK)

        self.display.blit(img_player, (self.head.x, self.head.y))

        for bullet in bullets:
            pygame.draw.circle(self.display, WHITE, (bullet.x, bullet.y), 20)
            if 1000 > bullet.x > 0:
                bullet.x -= 5
            else:
                bullets.pop(bullets.index(bullet))
                self.score += 1


        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):
        # [straight, right, left]

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]  # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]  # right turn r -> d -> l -> u
        else:  # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]  # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)
