import math
import time
import pygame
import random
pygame.init()

# can change this later to be depending on screen size
WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

def main():
  run = True

  # check for if if the quit button is clicked
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
  pygame.quit()


if __name__ == "__main__":
  main()