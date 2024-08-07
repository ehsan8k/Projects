import pygame
import math
import random
from pygame import mixer

# Initialize pygame and the mixer module for sound
pygame.init()
pygame.mixer.init()

# Create a game window with dimensions 800x500
screen = pygame.display.set_mode((800, 500))

# Load and set the background image for the game
background = pygame.image.load('Space.jpg')

# Load and play background music in an infinite loop
mixer.music.load('Background.wav')
mixer.music.play(-1)

# Set the caption of the game window
pygame.display.set_caption("Alien Invasion Game")

# Load and set the icon for the game window
icon = pygame.image.load('ship.png')
pygame.display.set_icon(icon)

# Explosion variables
explosion_frames = 30
explosion_current_frame = 0
explosion_scale = 1.0
explosion_alpha = 255

def reset_game():
    """Reset game state to initial conditions."""
    global ship_position_x, ship_position_y, Abs_position_x, bullet_position_x, bullet_position_y, bullet_state, score, Enemy_position_x, Enemy_position_y, Abs_Enemy_position_X, Abs_Enemy_position_Y, Enemy_bullets, explosion_current_frame, explosion_scale, explosion_alpha
    
    # Reset the spaceship position
    ship_position_x = 380
    ship_position_y = 390
    Abs_position_x = 0

    # Reset the bullet
    bullet_position_x = 0
    bullet_position_y = ship_position_y
    bullet_state = 'ready'

    # Reset the score
    score = 0

    # Reset enemy positions and bullets
    Enemy_position_x = [random.randint(0, 800 - 35) for _ in range(number_of_enemies)]
    Enemy_position_y = [random.randint(50, 150) for _ in range(number_of_enemies)]
    Abs_Enemy_position_X = [0.3 for _ in range(number_of_enemies)]
    Abs_Enemy_position_Y = [35 for _ in range(number_of_enemies)]
    Enemy_bullets = [{'x': Enemy_position_x[i], 'y': Enemy_position_y[i], 'state': 'ready'} for i in range(number_of_enemies)]

    # Reset explosion variables
    explosion_current_frame = 0
    explosion_scale = 1.0
    explosion_alpha = 255

# Load the spaceship image and scale it
ship = pygame.image.load('ship.png')
ship_width, ship_height = 35, 50
ship = pygame.transform.scale(ship, (ship_width, ship_height))

# Load and scale the bullet image
try:
    bullet = pygame.image.load('bullet.png')
except pygame.error as e:
    print("Error loading bullet image:", e)
    pygame.quit()
    exit()
bullet_width, bullet_height = 35, 40
bullet = pygame.transform.scale(bullet, (bullet_width, bullet_height))

# load and scale the explosion image
try:
    Explosion_image = pygame.image.load('explosion.png')
except pygame.error as e:
    print("Error loading explosion " ,e)
    pygame.quit()
    exit()

explosion_width, explosion_height = 64, 64 # Adjust the dimensions as needed
Explosion_image = pygame.transform.scale(Explosion_image, (explosion_width, explosion_height))

# Initializing explosion Variables
explosion_state = 'inactive'
explosion_position_x = 0
explosion_position_y = 0
explosion_timer = 0
try:
    explosion_sound = mixer.Sound('medium-explosion-40472.wav')
except pygame.error as e:
    print("Error loading explosion sound:", e)
    pygame.quit()
    exit()

# Load and scale the enemy image
enemy_img = pygame.image.load('enemy.png')
enemy_width, enemy_height = 35, 40
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))

# Initialize font for displaying the score
font = pygame.font.SysFont(None, 36)

# Initialize game state variables
number_of_enemies = 8
reset_game()

# Function to draw the player's spaceship
def player(x, y):
    screen.blit(ship, (x, y))

# Function to draw an enemy ship
def Enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Function to draw a bullet and set its state to 'fire'
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, (x, y))

# Function to check if there is a collision between two points
def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    return distance < 27

# Function to display the score on the screen
def show_score(x, y):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
    screen.blit(score_text, (x, y))

# Function to display a "Game Over" message
def show_game_over():
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))  # Red color
    screen.blit(game_over_text, (350, 250))  # Centered on the screen
    restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    screen.blit(restart_text, (230, 300))  # Instructions for restarting or quitting

running = True
game_over = False

while running:
    # Fill the screen with background color
    screen.fill((32, 178, 170))

    # Set a background image
    screen.blit(background, (0, 0))

    # Event handling for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Abs_position_x += 2 # Move spaceship right
            elif event.key == pygame.K_LEFT:
                Abs_position_x -= 2  # Move spaceship left
            elif event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_Sound = mixer.Sound('laser-45816.wav')
                bullet_Sound.play()
                bullet_position_x = ship_position_x + ship_width // 2 - bullet_width // 2
                bullet_position_y = ship_position_y
                bullet_state = 'fire'
            elif event.key == pygame.K_r and game_over:
                reset_game()
                game_over = False  # Reset game over flag
            elif event.key == pygame.K_q and game_over:
                running = False  # Quit the game

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                Abs_position_x = 0  # Stop spaceship movement

    if not game_over:
        # Update the spaceship's position and enforce boundaries
        ship_position_x += Abs_position_x
        if ship_position_x <= 0:
            ship_position_x = 0
        elif ship_position_x >= 754:
            ship_position_x = 754

        # Update enemy positions and check for collisions
        for i in range(number_of_enemies):
            Enemy_position_x[i] += Abs_Enemy_position_X[i]
            if Enemy_position_x[i] <= 0:
                Abs_Enemy_position_X[i] = 0.3
                Enemy_position_y[i] += Abs_Enemy_position_Y[i]
            elif Enemy_position_x[i] >= 765:
                Abs_Enemy_position_X[i] = -0.3
                Enemy_position_y[i] += Abs_Enemy_position_Y[i]

            # Check for collision between the bullet and the enemy
            if bullet_state == 'fire' and isCollision(Enemy_position_x[i], Enemy_position_y[i], bullet_position_x, bullet_position_y):
                explosion_position_x = Enemy_position_x[i]
                explosion_position_y = Enemy_position_y[i]
                explosion_state = 'active'
                explosion_current_frame = 0  # Reset the explosion animation
                explosion_sound.play()
                bullet_state = 'ready'
                bullet_position_y = ship_position_y
                score += 1
                Enemy_position_x[i] = random.randint(0, 800 - 35)
                Enemy_position_y[i] = random.randint(50, 150)

            # Draw the enemy ship
            Enemy(Enemy_position_x[i], Enemy_position_y[i])

            # Enemy shooting logic
            if random.randint(0, 100) < 2:  # Random chance for the enemy to shoot
                if Enemy_bullets[i]['state'] == 'ready':
                    Enemy_bullets[i] = {'x': Enemy_position_x[i] + 17, 'y': Enemy_position_y[i] + 35, 'state': 'fire'}
            
            # Move enemy bullets
            if Enemy_bullets[i]['state'] == 'fire':
                pygame.draw.rect(screen, (255, 0, 0), (Enemy_bullets[i]['x'], Enemy_bullets[i]['y'], bullet_width // 2, bullet_height // 2))
                Enemy_bullets[i]['y'] += 0.1  # Move bullet down
                if Enemy_bullets[i]['y'] > 500:
                    Enemy_bullets[i]['state'] = 'ready'
            
            # Check if enemy bullets collide with the player
            if Enemy_bullets[i]['state'] == 'fire' and isCollision(Enemy_bullets[i]['x'], Enemy_bullets[i]['y'], ship_position_x, ship_position_y):
                Explosion_Sound = mixer.Sound('medium-explosion-40472.wav')
                Explosion_Sound.play()
                game_over = True  # Set game over flag

        # Bullet movement
        if bullet_state == 'fire':
            fire_bullet(bullet_position_x, bullet_position_y)
            bullet_position_y -= 3  # Move the bullet up
            if bullet_position_y <= 0:
                bullet_state = 'ready'
                bullet_position_y = ship_position_y

        # Draw the player's spaceship
        player(ship_position_x, ship_position_y)

        # Display the current score
        show_score(10, 10)

        # Handle explosion animation
        if explosion_state == 'active':
            # Create a copy of the explosion image for manipulation
            current_explosion = Explosion_image.copy()
            
            # Scale the explosion
            scale = 1.0 + (explosion_current_frame / explosion_frames) * 0.5  # Grow up to 1.5x original size
            scaled_size = (int(explosion_width * scale), int(explosion_height * scale))
            current_explosion = pygame.transform.scale(current_explosion, scaled_size)
            
            # Fade out the explosion
            current_explosion.set_alpha(255 - (explosion_current_frame / explosion_frames) * 255)
            
            # Calculate position to keep explosion centered
            exp_x = explosion_position_x - (scaled_size[0] - explosion_width) / 2
            exp_y = explosion_position_y - (scaled_size[1] - explosion_height) / 2
            
            # Draw the explosion
            screen.blit(current_explosion, (exp_x, exp_y))
            
            # Update explosion frame
            explosion_current_frame += 1
            if explosion_current_frame >= explosion_frames:
                explosion_state = 'inactive'
                explosion_current_frame = 0

    else:
        # Display "Game Over" message and restart options
        show_game_over()

    # Update the display
    pygame.display.update()

# Quit pygame and close the window
pygame.quit()