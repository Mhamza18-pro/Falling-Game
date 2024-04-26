import pygame
import random
import Randomization


# Initialize Pygame
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catching Falling Objects')

# Define colors and game properties
background_color = pygame.image.load('GameAssets/SEO_GoldIngots.png').convert_alpha()
object_color = pygame.image.load('GameAssets/SEO_GoldIngots.png').convert_alpha()
player_color = (0, 0, 255)
object_size, player_size = 50, 50
object_x = random.randint(0, screen_width - object_size)
object_y = 0
object_speed = 10
player_x = screen_width // 2
player_y = screen_height - player_size
is_paused = False  # Initialize pause state
object_rand_value= random.randint(1,20) #Initialized a new variable to store a random value in the object falling

# initializing a score variable
score=0

# initializing variable to use in drawing the number on the object

font = pygame.font.Font(None, 36)
white = (255, 255, 255)
black = (0, 0, 0)

# Game clock
clock = pygame.time.Clock()

# Timer
counter, timer_text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT,1000)
timer_font = pygame.font.Font(None,30)

# Math Problem Variables
randomNum1 = random.randint(0,20)
randomNum2 = random.randint(0,20)
listOfOperations = ["x", "+", "-", "/"]
i = random.randint(0,3)
randomOperation = listOfOperations[i]

# Random Math Problems
math_problems_font = pygame.font.Font(None, 30)
math_problems_text = str(Randomization.showProblem(randomNum1, randomNum2, randomOperation))
number = Randomization.randomSequence(randomNum1, randomNum2, randomOperation)


running = True
while running:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.USEREVENT:
      counter -= 1
      timer_text = str(counter).rjust(3) if counter > 0 else "Time's Up!" 
      if counter == -2:
        running = False
  
  # Game logic when not paused
  if not is_paused:
    object_y += object_speed
    
    if object_y > screen_height:
      
      # Creates new falling object
      object_x = random.randint(0, screen_width - object_size)
      object_y = 0
      number +=1
    
    if player_y < object_y + object_size and player_x < object_x + object_size and player_x + player_size > object_x:
      object_x = random.randint(0, screen_width - object_size)
      object_y = 0
  
  screen.fill(background_color)
  screen.blit(object_color, (object_x, object_y),(100,100,100,100))
  # pygame.draw.rect(screen, object_color,
  #                  (object_x, object_y, object_size, object_size))
  

  #Add the timer to the screen 
  screen.blit(timer_font.render(timer_text, True, black), (32,48))

  #Add the math problems to the screen
  screen.blit(timer_font.render(math_problems_text, True, black), (350,32))
  
  # Implements code for counting score
  if not is_paused:
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (510, 20))
  else:
    pause_text = font.render("Paused - Press Space to Resume", True, (0, 0, 0))
    screen.blit(pause_text, (screen_width // 2 - 200, screen_height // 2))
  
  # Draws a value on the object as it falls
  text_surface = font.render(str(number), True, black)
  text_rect = text_surface.get_rect(center=(object_x + object_size // 2, object_y + object_size // 2))
  screen.blit(text_surface, text_rect)
  
  pygame.display.flip()
  clock.tick(10) #the number you put in parentheses effects the speed the coin falls


pygame.quit()
