import pygame

pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Test")

# Colors
background_color = (30, 30, 30)  # Dark gray
circle_color = (255, 0, 0)       # Red

# Circle properties
circle_x, circle_y = width // 2, height // 2
circle_radius = 30
circle_speed = 2

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            pygame.quit()
            sys.exit()
    
    # Update circle position
    circle_x += circle_speed
    if circle_x > width or circle_x < 0:
        circle_speed = -circle_speed  # Reverse direction
    
    # Draw everything
    screen.fill(background_color)  # Clear screen
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.display.flip()  # Update display
    
    # Cap the frame rate
    clock.tick(60)