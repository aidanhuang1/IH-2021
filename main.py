
import random
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800), 0)
pygame.display.set_caption("Pygame test")

width = screen.get_width()
height = screen.get_height()
centreX = int(width / 2)
centreY = int(height / 2)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colour = RED


img = pygame.image.load("Jet.png")
img = pygame.transform.scale(img, (25,25))
img_rect = img.get_rect()
img_rect.center = (700, 700)




# Method to change the colour (rgb)
def colourchange():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# first set up your font (typeface and size)
# I have created two different ones here that can be used later in the program
font_test = pygame.font.SysFont("arial", 60)

main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                centreX = width / 2
                centreY = height / 2
                colour = colourchange()
            if event.key == pygame.K_UP:
                centreY -= 20
                colour = colourchange()
            if event.key == pygame.K_DOWN:
                centreY += 20
                colour = colourchange()
            if event.key == pygame.K_LEFT:
                centreX -= 20
                colour = colourchange()
            if event.key == pygame.K_RIGHT:
                centreX += 20
                colour = colourchange()

    # render the text into an image of the text, colour is red
    # school = font_test.render(img, True, img_rect)
    # create a rect from the text
    # textRect = img.get_rect()
    
    # place this rect at the centre of the screen
    img_rect.center = (centreX, centreY)
    if centreX > width - width / 6:
        centreX = width - width / 6
    if centreX < width / 5:
        centreX = width / 5
    if centreY > height - height / 7:
        centreY = height - height / 7
    if centreY < height / 20:
        centreY = height / 20

    # blit the image to memory, it will display upon next update
    screen.blit(img, img_rect)
    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
sys.exit()
