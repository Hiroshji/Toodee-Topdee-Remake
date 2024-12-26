import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) # outline color
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toodee and Topdee")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Character properties
CHARACTER_SIZE = 50
TOODEE_POS = [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2]
TOPDEE_POS = [SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT // 2]

# Movement flags
TOODEE_GRAVITY = True  # Toodee affected by gravity (platformer mode)
TOPDEE_GRAVITY = False  # Topdee ignores gravity (top-down mode)

SPEED = 5
GRAVITY = 0.5
JUMP_SPEED = -10

# Initialize vertical velocity
vertical_velocity = 0

# Current character (0 for Toodee, 1 for Topdee)
current_character = 0

def draw_character(screen, color, pos, highlight):
    pygame.draw.rect(screen, color, (*pos, CHARACTER_SIZE, CHARACTER_SIZE))
    if highlight:
        pygame.draw.rect(screen, BLACK, (*pos, CHARACTER_SIZE, CHARACTER_SIZE), 3)

def apply_gravity(pos):
    if pos[1] + CHARACTER_SIZE < SCREEN_HEIGHT:
        pos[1] += GRAVITY

def handle_toodee_controls(keys, pos):
    global vertical_velocity

    if keys[pygame.K_UP]:
        if pos[1] + CHARACTER_SIZE >= SCREEN_HEIGHT:  # Allow jumping only when on the ground
            vertical_velocity = JUMP_SPEED

    # Apply gravity
    vertical_velocity += GRAVITY
    pos[1] += vertical_velocity

    # Ensure Toodee doesn't fall through the ground
    if pos[1] + CHARACTER_SIZE >= SCREEN_HEIGHT:
        pos[1] = SCREEN_HEIGHT - CHARACTER_SIZE
        vertical_velocity = 0

    if keys[pygame.K_LEFT]:
        pos[0] = max(0, pos[0] - SPEED)
    if keys[pygame.K_RIGHT]:
        pos[0] = min(SCREEN_WIDTH - CHARACTER_SIZE, pos[0] + SPEED)

def handle_topdee_controls(keys, pos):
    if keys[pygame.K_w]:
        pos[1] = max(0, pos[1] - SPEED)
    if keys[pygame.K_s]:
        pos[1] = min(SCREEN_HEIGHT - CHARACTER_SIZE, pos[1] + SPEED)
    if keys[pygame.K_a]:
        pos[0] = max(0, pos[0] - SPEED)
    if keys[pygame.K_d]:
        pos[0] = min(SCREEN_WIDTH - CHARACTER_SIZE, pos[0] + SPEED)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Switch character on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                current_character = 1 - current_character

    # Handle movement
    keys = pygame.key.get_pressed()

    if current_character == 0:  # Toodee's controls (platformer)
        handle_toodee_controls(keys, TOODEE_POS)
        if TOODEE_GRAVITY:
            apply_gravity(TOODEE_POS)

    elif current_character == 1:  # Topdee's controls (top-down)
        handle_topdee_controls(keys, TOPDEE_POS)

    # Ensure Toodee doesn't fall below the screen
    TOODEE_POS[1] = min(SCREEN_HEIGHT - CHARACTER_SIZE, TOODEE_POS[1])

    # Clear the screen
    screen.fill(WHITE)

    # Draw Toodee and Topdee
    draw_character(screen, BLUE, TOODEE_POS, current_character == 0)
    draw_character(screen, RED, TOPDEE_POS, current_character == 1)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
