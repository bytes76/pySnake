import pygame
import random
import time

# How fast the snake is goin
snakeSpeed = 20

# Window size, width & height
window = [500, 500]

# Initialising pygame & window
pygame.init()
pygame.display.set_caption('pySnake')
boundaries = pygame.display.set_mode((window[0], window[1]))
fps = pygame.time.Clock()

# Default snake location
snakeLoc = [window[0] / 2, window[1] / 2]

# Create the first few segments of the snake to begin with
snakeSegment = [[snakeLoc[0], snakeLoc[1]], [snakeLoc[0] - 10, snakeLoc[1]], [snakeLoc[0] - 10, snakeLoc[1]], [snakeLoc[0] - 10, snakeLoc[1]]]

# Fruit location, making it random
fruitLoc = [random.randrange(1, (window[0] // 10)) * 10, random.randrange(1, (window[1] // 10)) * 10]
isFruitSpawned = True

# Start with right direction first
direction = 'RIGHT'
changeDirection = direction
score = 0

# Draw the score on screen
def Score(choice, color, font, size):
	scoreFont = pygame.font.SysFont(font, size)
	scoreSurface = scoreFont.render('Fruits eaten: ' + str(score), True, color) # Convert int score to a string
	scoreRect = scoreSurface.get_rect()
	boundaries.blit(scoreSurface, scoreRect)

# End the program
def Terminate():
	# Quit program
	time.sleep(3)
	pygame.quit()
	quit()

# On repeat
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				changeDirection = 'UP'
			if event.key == pygame.K_DOWN:
				changeDirection = 'DOWN'
			if event.key == pygame.K_LEFT:
				changeDirection = 'LEFT'
			if event.key == pygame.K_RIGHT:
				changeDirection = 'RIGHT'

	# Ensure cases where 2+ keys are pressed at once do not intefere, not logical
	if changeDirection == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if changeDirection == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if changeDirection == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if changeDirection == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snakeLoc[1] -= 10
	if direction == 'DOWN':
		snakeLoc[1] += 10
	if direction == 'LEFT':
		snakeLoc[0] -= 10
	if direction == 'RIGHT':
		snakeLoc[0] += 10

	snakeSegment.insert(0, list(snakeLoc))

	# When snake location = fruit location (snake eats fruit)
	if snakeLoc[0] == fruitLoc[0] and snakeLoc[1] == fruitLoc[1]:
		score += 1
		isFruitSpawned = False

	else:
		snakeSegment.pop()
		
	if not isFruitSpawned:
		fruitLoc = [random.randrange(1, (window[0] // 10)) * 10, random.randrange(1, (window[1] // 10)) * 10]
		
	isFruitSpawned = True
	boundaries.fill(pygame.Color(0, 0, 0))
	
	for pos in snakeSegment:
		pygame.draw.rect(boundaries, pygame.Color(255, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

	pygame.draw.rect(boundaries, pygame.Color(255, 0, 0), pygame.Rect(fruitLoc[0], fruitLoc[1], 10, 10))

	if snakeLoc[0] < 0 or snakeLoc[0] > window[0] - 10:
		Terminate()

	if snakeLoc[1] < 0 or snakeLoc[1] > window[1] - 10:
		Terminate()

	for block in snakeSegment[1:]:
		if snakeLoc[0] == block[0] and snakeLoc[1] == block[1]:
			Terminate()

	# Update everything & score
	Score(1, pygame.Color(255, 255, 255), 'times new roman', 20)
	pygame.display.update()
	fps.tick(snakeSpeed)