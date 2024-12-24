import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toodee and Topdee")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Character properties
CHARACTER_SIZE = 40
TOODEE_POS = [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2]
TOPDEE_POS = [SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT // 2]

SPEED = 5

# Current character (0 for Toodee, 1 for Topdee)
current_character = 0

def draw_character(screen, color, pos, highlight):
    pygame.draw.rect(screen, color, (*pos, CHARACTER_SIZE, CHARACTER_SIZE))
    if highlight:
        pygame.draw.rect(screen, BLACK, (*pos, CHARACTER_SIZE, CHARACTER_SIZE), 3)

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

    if current_character == 0:  # Toodee's controls
        if keys[pygame.K_UP]:
            TOODEE_POS[1] = max(0, TOODEE_POS[1] - SPEED)
        if keys[pygame.K_DOWN]:
            TOODEE_POS[1] = min(SCREEN_HEIGHT - CHARACTER_SIZE, TOODEE_POS[1] + SPEED)
        if keys[pygame.K_LEFT]:
            TOODEE_POS[0] = max(0, TOODEE_POS[0] - SPEED)
        if keys[pygame.K_RIGHT]:
            TOODEE_POS[0] = min(SCREEN_WIDTH - CHARACTER_SIZE, TOODEE_POS[0] + SPEED)

    elif current_character == 1:  # Topdee's controls
        if keys[pygame.K_w]:
            TOPDEE_POS[1] = max(0, TOPDEE_POS[1] - SPEED)
        if keys[pygame.K_s]:
            TOPDEE_POS[1] = min(SCREEN_HEIGHT - CHARACTER_SIZE, TOPDEE_POS[1] + SPEED)
        if keys[pygame.K_a]:
            TOPDEE_POS[0] = max(0, TOPDEE_POS[0] - SPEED)
        if keys[pygame.K_d]:
            TOPDEE_POS[0] = min(SCREEN_WIDTH - CHARACTER_SIZE, TOPDEE_POS[0] + SPEED)

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
