import pygame
import random

# Initialize Pygame
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catching Falling Objects')

# Define colors and game properties
background_color = (255, 255, 255)
object_color = (255, 0, 0)
player_color = (0, 0, 255)
object_size, player_size = 50, 50
object_x = random.randint(0, screen_width - object_size)
object_y = 0
object_speed = 10
player_x = screen_width // 2
player_y = screen_height - player_size
is_paused = False  # Initialize pause state
object_rand_value= random.randint(1,20) #Initialized a new variable to store a random value in the object falling

# Game clock
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Game logic when not paused
  if not is_paused:
    object_y += object_speed
    if object_y > screen_height:
      running = False  # End the game
    if player_y < object_y + object_size and player_x < object_x + object_size and player_x + player_size > object_x:
      object_x = random.randint(0, screen_width - object_size)
      object_y = 0
  
  screen.fill(background_color)
  pygame.draw.rect(screen, object_color,
                   (object_x, object_y, object_size, object_size))

  pygame.display.flip()
  clock.tick(30)


pygame.quit()