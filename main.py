import pygame
import random
import Randomization


# Initialize Pygame
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catching Falling Objects')

# Define colors and game properties
background_color = pygame.image.load('GameAssets/7-Little_Helpers-Rainbow_City.webp').convert_alpha()
object_color = pygame.image.load('GameAssets/SEO_GoldIngots.png').convert_alpha()
player_color = pygame.image.load('GameAssets/SEO_Leprechaun.png').convert_alpha()
object_size, player_size = 50, 200
object_x = random.randint(0, screen_width - object_size)
object_y = 0
object_speed = 10
player_x = screen_width // 2
player_y = screen_height - player_size
player_speed = 10
is_paused = False  # Initialize pause state

# initializing a score variable
score=0

# initializing variable to use in drawing the number on the object

font = pygame.font.Font(None, 36)
white = (255, 255, 255)
black = (0, 0, 0)

# Game clock
clock = pygame.time.Clock()

# Timer
counter, timer_text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT,1000)
timer_font = pygame.font.Font(None,50)

# Math Problem Variables
randomNum1 = random.randint(0,20)
randomNum2 = random.randint(0,20)
listOfOperations = ["x", "+", "-", "/"]
i = random.randint(0,3)
randomOperation = listOfOperations[i]

# Random Math Problems
math_problems_font = pygame.font.Font(None, 30)
math_problems_text = str(Randomization.showProblem(randomNum1, randomNum2,randomOperation))

# Gold ignot falls with a random number initially
number = random.randint(-100,100)

# Variable to track key states
key_states = {pygame.K_LEFT: False, pygame.K_RIGHT: False}
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
  # Enables the player's movement
    if event.type == pygame.KEYDOWN:
      if event.key in key_states:
          key_states[event.key] = True
      if event.key == pygame.K_SPACE:
          is_paused = not is_paused
    if event.type == pygame.KEYUP:
      if event.key in key_states:
            key_states[event.key] = False

  # Update player position based on key states
  if key_states[pygame.K_LEFT] and player_x > 0:
      player_x -= player_speed
  if key_states[pygame.K_RIGHT] and player_x < screen_width - player_size:
      player_x += player_speed

  # Game logic when not paused
  if not is_paused:
    object_y += object_speed
    probability = random.randint(0,50)
   

    if object_y > screen_height:
  

      # Creates new falling object
      object_x = random.randint(0, screen_width - object_size)
      object_y = 1

      #There is a 50% chance that the falling object will be the right answer
      #generates a new probabiiliy each time item fall off screen
      print(probability)
      if(probability%2 == 0):
        number = Randomization.randomSequence(randomNum1, randomNum2, randomOperation)
      else:
        number = random.randint(-100,100)

    if player_y < object_y + object_size and player_x < object_x + object_size and player_x + player_size > object_x: 
      if number == Randomization.randomSequence(randomNum1, randomNum2, randomOperation):
        score += 100 #incease score and player speed if the number is correct 
        player_speed += 5
        object_x = random.randint(0, screen_width - object_size)
        object_y = 0
        # generate a new problem each time the player get a correct answer
        randomNum1 = random.randint(0,20)
        randomNum2 = random.randint(0,20)
        listOfOperations = ["x", "+", "-", "/"]
        i = random.randint(0,3)
        randomOperation = listOfOperations[i]
        # Random Math Problems
        math_problems_font = pygame.font.Font(None, 30)
        math_problems_text = str(Randomization.showProblem(randomNum1, randomNum2, randomOperation))
      else: #decreases score if the player is incorrect
        score -= 50 
        object_x = random.randint(0, screen_width - object_size)
        object_y = 0
        if(probability%2 == 0): #generates a new number is the number is wrong
          number = Randomization.randomSequence(randomNum1, randomNum2, randomOperation)
        else:
          number = random.randint(-100,100)



  screen.blit(background_color,(0,0))
  screen.blit(object_color, (object_x, object_y))
  screen.blit(player_color, (player_x, player_y))
  #Add the timer to the screen 
  screen.blit(timer_font.render(timer_text, True, black), (32,48))

  #Add the math problems to the screen
  screen.blit(timer_font.render(math_problems_text, True, black), (350,32))

  # Implements code for counting score
  text = font.render("Score: " + str(score), True, (0, 0, 0))
  screen.blit(text, (600, 40))
  
  if is_paused:
    pause_text = font.render("Paused - Press Space to Resume", True, (0, 0, 0))
    screen.blit(pause_text, (screen_width // 2 - 200, screen_height // 2))

  # Draws a value on the object as it falls
  text_surface = font.render(str(number), True, black)
  text_rect = text_surface.get_rect(center=(object_x + object_size // 2, object_y + object_size // 2))
  screen.blit(text_surface, text_rect)

  pygame.display.flip()
  clock.tick(20) #the number you put in parentheses effects the speed the coin falls


pygame.quit()
